from . import convert

import argparse
import json
import sys


assert __name__ == '__main__'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file', type=argparse.FileType('r'),
        nargs='?', default=sys.stdin,
        help='file as input'
    )
    parser.add_argument(
        '--load', type=argparse.FileType('r'),
        help='json file to add into convert table'
    )
    
    args = parser.parse_args()

    if args.load:
        print(f'load for {args.load.name}...')
        convert.update_transtable(
            json.load(args.load)
        )

    if args.file is sys.stdin:
        repl()
    else:
        print(
            convert.convert(args.file.read())
        )


def repl():
    print('Roman >>> ', end='', flush=True)
    
    for sentence in map(str.rstrip, sys.stdin):
        print(
            'JKana ... {}'.format(convert.convert(sentence))
        )
        print('Roman >>> ', end='', flush=True)


main()
