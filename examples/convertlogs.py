#!/usr/bin/env python3
#   encoding: utf8
#   convertlogs.py

import logging

from argparse import ArgumentParser
from datetime import datetime
from itertools import islice
from os.path import realpath, splitext
from shlex import shlex
from tskv import dump


def tokenize_line(line):
    tokens = shlex(line)

    ip = ''.join(islice(tokens, 7))
    _, _ = islice(tokens, 2)

    _ = tokens.get_token()
    ds = ''.join(islice(tokens, 11))
    tz = ''.join(islice(tokens, 2))
    _ = tokens.get_token()

    ds_tz = ds, tz

    request = tokens.get_token()
    status_code, content_size = islice(tokens, 2)
    referer = tokens.get_token()
    user_agent = tokens.get_token()

    return (ip, ds_tz, request, status_code, content_size, referer, user_agent)

def parse_line(line):
    ident = lambda x: x
    unquote = lambda x: x[1:-1]
    cast = (
        ident,
        lambda x: datetime.strptime(''.join(x), '%d/%b/%Y:%H:%M:%S%z'),
        unquote,
        int,
        int,
        unquote,
        unquote,
    )

    tokens = tokenize_line(line)
    row = list(k(v) for k, v in zip(cast, tokens))

    return row

def make_record(row):
    keys = (
        'ip',
        'timestamp',
        'request',
        'status_code',
        'content_length',
        'referer',
        'user_agent')
    return dict(zip(keys, row))

def convert_log(input_filename, output_filename):
    logging.info('converting logs to tskv format...')
    logging.info('read raw logs from `%s`', input_filename)
    logging.info('write tskv logs to `%s`', output_filename)

    with \
        open(input_filename, 'r') as fin, \
        open(output_filename, 'w') as fout:
            for i, line in enumerate(fin, 1):
                if i % 10 == 0:
                    logging.info('%d rows proccessed', i)

                row = parse_line(line)
                rec = make_record(row)

                dump(rec, fout)

    logging.info('done')

def main():
    logging.basicConfig(
        format='%(asctime)s %(filename)s %(levelname)s %(message)s',
        level=logging.INFO)

    parser = ArgumentParser(
            description='Convert nginx logs to tskv-formated logs.')
    parser.add_argument('-i', '--input', default='access.log', help='path to raw logs')
    parser.add_argument('-o', '--output', help='path to converted logs')

    args = parser.parse_args()

    input_filename = realpath(args.input)

    if args.output:
        output_filename = realpath(args.output)
    else:
        root, ext = splitext(input_filename)
        output_filename = ''.join((root, '.tskv'))

    convert_log(input_filename, output_filename)


if __name__ == '__main__':
    main()
