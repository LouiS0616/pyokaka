from .convert import convert
from .convert import update_transtable

import argparse
import json
import sys


assert __name__ == '__main__'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file', type=argparse.FileType('r', encoding='utf-8'),
        nargs='?', default=sys.stdin,
        help='file as input'
    )
    parser.add_argument(
        '--load', type=argparse.FileType('r', encoding='utf-8'),
        metavar='JSONFILE',
        help='json file (UTF-8) to add into convert table'
    )

    args = parser.parse_args()

    if args.load:
        print(f'load for {args.load.name}...')

        try:
            transtable = json.load(args.load)
        except UnicodeDecodeError:
            print(
                'json file must be written in utf-8 encoding.',
                file=sys.stderr
            )
            sys.exit(1)

        update_transtable(transtable)

    if args.file is sys.stdin:
        repl()
    else:
        print(
            convert(args.file.read())
        )


def repl():
    print('Roman >>> ', end='', flush=True)

    for sentence in map(str.rstrip, sys.stdin):
        print(
            'JKana ... {}'.format(convert(sentence))
        )
        print('Roman >>> ', end='', flush=True)


main()
