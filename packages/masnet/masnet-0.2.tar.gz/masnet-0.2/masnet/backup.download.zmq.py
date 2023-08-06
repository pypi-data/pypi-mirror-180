# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=global-statement
# pylint: disable=bare-except,broad-except
import argparse
import http
import gzip
import json
import os
import sys
import time
from threading import Thread
import traceback
from urllib.error import URLError, HTTPError
import urllib.request
import zmq
from masnet import __version__


VERBOSE = False
OUTPUT_DIR = None
CONTROL_URL = 'inproc://control'
ERROR_URL = 'inproc://download_error'
DOWNLOAD_PEERS_READY_URL = 'inproc://download_peers_ready'
DOWNLOAD_PEERS_JSON_URL = 'inproc://download_peers_json'
DECODE_PEERS_JSON_URL = 'inproc://decode_peers_json'
PROCESS_PEERS_URL = 'inproc://process_peers'


def verbose(s):
    if VERBOSE:
        print(s, flush=True)


def get_path(fname):
    return os.path.join(OUTPUT_DIR, fname)


def read_json(sock):
    try:
        return sock.recv_json(zmq.NOBLOCK)
    except zmq.ZMQError as e:
        if e.errno == zmq.EAGAIN:
            return None
        else:
            raise


def read_string(sock):
    try:
        return sock.recv_string(zmq.NOBLOCK)
    except zmq.ZMQError as e:
        if e.errno == zmq.EAGAIN:
            return None
        else:
            raise

def send_json(sock, json):
    try:
        sock.send_json(json, zmq.NOBLOCK)
        return True
    except zmq.ZMQError as e:
        if e.errno == zmq.EAGAIN:
            return False
        else:
            raise


def send_string(sock, s):
    try:
        sock.recv_string(s, zmq.NOBLOCK)
        return True
    except zmq.ZMQError as e:
        if e.errno == zmq.EAGAIN:
            return False
        else:
            raise

def error_handler(ctx,
                  idx,
                  timeout=-1):

    verbose('error handler.%d entry.' % idx)

    sock_control = ctx.socket(zmq.SUB)
    sock_control.connect(CONTROL_URL)
    sock_control.setsockopt_string(zmq.SUBSCRIBE, '*')
    sock_control.setsockopt_string(zmq.SUBSCRIBE, 'error_handler')

    sock_error = ctx.socket(zmq.PULL)
    sock_error.bind(ERROR_URL)

    verbose('error handler.%d ready...' % idx)

    while True:
        try:
            cmd = read_string(sock_control)
            if cmd is not None:
                if cmd == 'quit':
                    print('error handler quit.')
                    while read_json(sock_error):
                        pass
                    return
            req = read_json(sock_error)
            if req is not None:
                domain = req['domain']
                err = req['err']
                print('ERROR: %s %s' % (req, err))
        except:
            traceback.print_exc()


def download(ctx,
             idx,
             timeout=-1):

    verbose('download.%d entry.' % idx)

    sock_control = ctx.socket(zmq.SUB)
    sock_control.connect(CONTROL_URL)
    sock_control.setsockopt_string(zmq.SUBSCRIBE, '*')
    sock_control.setsockopt_string(zmq.SUBSCRIBE, 'download')

    sock_download_peers_json = ctx.socket(zmq.PULL)
    sock_download_peers_json.connect(DOWNLOAD_PEERS_JSON_URL)

    sock_error = ctx.socket(zmq.PUSH)
    sock_error.connect(ERROR_URL)

    sock_download_peers_ready = ctx.socket(zmq.PUSH)
    sock_download_peers_ready.connect(DOWNLOAD_PEERS_READY_URL)

    sock_decode_peers_json = ctx.socket(zmq.PUSH)
    sock_decode_peers_json.bind(DECODE_PEERS_JSON_URL)

    verbose('download.%d ready...' % idx)

    while True:
        try:
            cmd = read_string(sock_control)
            if cmd is not None:
                if cmd == 'quit':
                    print('download quit.')
                    while read_string(sock_download_peers_json):
                        pass
                    return
            domain = read_string(sock_download_peers_json)
            if domain is not None:
                print('download %s' % domain)
                peers_url = 'https://%s/api/v1/instance/peers' % domain
                res = None
                err = None
                try:
                    if timeout > 0:
                        with urllib.request.urlopen(peers_url,
                                                    timeout=timeout) as req:
                            res = req.read().decode('utf-8')
                    else:
                        with urllib.request.urlopen(peers_url) as req:
                            res = req.read().decode('utf-8')
                except HTTPError as e:
                    err = e.__class__.__name__
                except URLError as e:
                    err = e.__class__.__name__
                if err is not None:
                    sock_error.send_json({'domain': domain,
                                          'err': err})
                elif res is not None:
                    sock_decode_peers_json.send_json({'domain': domain,
                                                      'peers_json': res})
                else:
                    raise Exception('why res is None?')
        except:
            traceback.print_exc()


def decode(ctx,
           idx):

    verbose('decode.%d entry.' % idx)

    sock_control = ctx.socket(zmq.SUB)
    sock_control.connect(CONTROL_URL)
    sock_control.setsockopt_string(zmq.SUBSCRIBE, '*')
    sock_control.setsockopt_string(zmq.SUBSCRIBE, 'decode')

    sock_decode_peers_json = ctx.socket(zmq.PULL)
    sock_decode_peers_json.connect(DECODE_PEERS_JSON_URL)

    sock_error = ctx.socket(zmq.PUSH)
    sock_error.connect(ERROR_URL)

    sock_process_peers = ctx.socket(zmq.PUSH)
    sock_process_peers.bind(PROCESS_PEERS_URL)

    verbose('decode.%d ready...' % idx)

    while True:
        try:
            cmd = read_string(sock_control)
            if cmd is not None:
                if cmd == 'quit':
                    print('decode quit.')
                    while read_json(sock_decode_peers_json):
                        pass
                    return
            req = read_json(sock_decode_peers_json)
            if req is not None:
                domain = req['domain']
                print('decode %s' % domain)
                try:
                    peers = json.loads(req['peers_json'])
                    peers_file = '%s.peers.json.gz' % domain
                    peers_file_path = get_path(peers_file)
                    peers_json = {'domain': domain, 'peers': peers}
                    with gzip.open(peers_file_path, 'wb') as f:
                        f.write(json.dumps(peers_json).encode('utf-8'))
                    sock_process_peers.send_json(peers_json)
                except json.JSONDecodeError as e:
                    err = e.__class__.__name__
                    sock_error.send_json({'domain': domain,
                                          'err': err})
        except:
            traceback.print_exc()



def process(ctx,
            idx,
            start_domain):

    verbose('process.%d entry.' % idx)

    sock_control = ctx.socket(zmq.SUB)
    sock_control.connect(CONTROL_URL)
    sock_control.setsockopt_string(zmq.SUBSCRIBE, '*')
    sock_control.setsockopt_string(zmq.SUBSCRIBE, 'process')

    sock_process_peers = ctx.socket(zmq.PULL)
    sock_process_peers.connect(PROCESS_PEERS_URL)

    sock_error = ctx.socket(zmq.PUSH)
    sock_error.connect(ERROR_URL)

    sock_download_peers_json = ctx.socket(zmq.PUSH)
    sock_download_peers_json.set_hwm(2)
    sock_download_peers_json.bind(DOWNLOAD_PEERS_JSON_URL)

    domains = set()

    verbose('process.%d ready...' % idx)

    verbose('sending start domain...')
    domains.add(start_domain)
    sock_download_peers_json.send_string(start_domain)

    while True:
        try:
            cmd = read_string(sock_control)
            if cmd is not None:
                if cmd == 'quit':
                    print('process quit.')
                    while read_json(sock_process_peers):
                        pass
                    return
            req = read_json(sock_process_peers)
            if req is not None:
                domain = req['domain']
                print('process %s' % domain)
                peers = req['peers']
                cnt_new_peers = 0
                for peer in peers:
                    # this is not needed, but just to handle bad responses safely
                    if peer is not None and len(peer) > 0:
                        if peer not in domains:
                            cnt_new_peers = cnt_new_peers + 1
                            domains.add(peer)
                            print('request to download: %s' % peer)
                            sock_download_peers_json.send_string(peer)
                            time.sleep(1)
                print("%s %d -> %d" % (domain, len(peers), cnt_new_peers))
        except:
            traceback.print_exc()

# pylint: disable=too-many-statements
def main():
    print('masnet v%s' % __version__)
    parser = argparse.ArgumentParser(prog='masnet.download',
                                     description='',
                                     epilog='')

    parser.add_argument('-d', '--discard',
                        help='discard cached files, redownloads everything (default: false)',
                        action='store_true',
                        required=False,
                        default=False)

    parser.add_argument('--demo',
                        help='run for a minute then no new visits is scheduled, use for demo',
                        action='store_true',
                        required=False,
                        default=False)

    parser.add_argument('-e', '--exclude-file',
                        help='exclude the domains and all of their ' \
                             'subdomains in the file specified (default: ' \
                             'None but activitypub-troll.cf, ' \
                             'misskey-forkbomb.cf, repl.co is excluded)',
                        required=False)

    parser.add_argument('-n', '--num-threads',
                        help='use specified number of Python threads (default: 100)',
                        type=int,
                        required=False,
                        default=100)

    parser.add_argument('-o', '--output-dir',
                        help='use specified directory for files, it creates ' \
                             'the directory if not exists ' \
                             '(default: current directory)',
                        required=False)

    parser.add_argument('--output-errors',
                        help='save list of errors encountered to file (default: errors.out)',
                        required=False,
                        default='errors.out')

    parser.add_argument('--output-skips',
                        help='save list of skipped domains due to exclusion (default: skips.out)',
                        required=False,
                        default='skips.out')

    parser.add_argument('--output-visits',
                        help='save list of visited domains to file (default: visits.out)',
                        required=False,
                        default='visits.out')

    parser.add_argument('-s', '--start-domain',
                        help='domains to start traversal from (default: mastodon.social)',
                        required=False,
                        default='mastodon.social')

    parser.add_argument('-t', '--timeout',
                        help='use specified number of seconds for timeout ' \
                             '(default: system default)',
                        type=int,
                        required=False,
                        default=-1)

    parser.add_argument('-v', '--verbose',
                        help='enable verbose logging, mostly for development',
                        action='store_true',
                        required=False,
                        default=False)

    args = parser.parse_args()

    global VERBOSE
    VERBOSE = args.verbose

    verbose(str(args))

    excluded = []
    if args.exclude_file is None:
        excluded = ['.activitypub-troll.cf',
                    '.misskey-forkbomb.cf',
                    '.repl.co']
    else:
        with open(args.exclude_file, 'r') as f:
            excluded.append(f.readline())

    if VERBOSE:
        verbose('--- start of excluded domains list ---')
        for excluded_domain in excluded:
            verbose(excluded_domain)
        verbose('--- end of excluded domains ---')

    global OUTPUT_DIR
    if args.output_dir is None:
        OUTPUT_DIR = os.getcwd()
    else:
        OUTPUT_DIR = os.path.abspath(args.output_dir)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    # reset files
    errorsfp = open(get_path(args.output_errors), 'w')
    skipsfp = open(get_path(args.output_skips), 'w')
    visitsfp = open(get_path(args.output_visits), 'w')

    with zmq.Context() as ctx:

        control_pub = ctx.socket(zmq.PUB)
        control_pub.bind(CONTROL_URL)

        t_downloads = list()

        for i in range(0, args.num_threads):
            t_downloads.append(Thread(target=download,
                                      args=[ctx,
                                            i,
                                            args.timeout]))

        t_decode = Thread(target=decode,
                          args=[ctx,
                                0])

        t_process = Thread(target=process,
                           args=[ctx,
                                 0,
                                 args.start_domain])

        t_error_handler = Thread(target=error_handler,
                                 args=[ctx,
                                       0])

        t_error_handler.start()
        for t_download in t_downloads:
            t_download.start()
        t_decode.start()
        t_process.start()

        try:
            while True:
                control_pub.send_string('ping')
                time.sleep(1)
        except KeyboardInterrupt:
            print('wait to all threads to terminate...')

        # wait till they quit, otherwise sockets might be closed etc.
        control_pub.send_string('* quit')

        for t_download in t_downloads:
            t_download.join()
        t_decode.join()
        t_process.join()
        t_error_handler.join()

    print('bye.')

if __name__ == '__main__':
    main()
