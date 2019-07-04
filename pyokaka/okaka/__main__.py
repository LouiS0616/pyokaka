from . import convert

import argparse
import sys


assert __name__ == '__main__'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file', type=argparse.FileType('r'),
        nargs='?', default=sys.stdin,
        help='file as input'
    )
    
    args = parser.parse_args()

    if args.file is sys.stdin:
        repl()
    else:
        print(
            convert.convert(args.file.read())
        )

def repl():
    print('>>> ', end='', flush=True)
    
    for sentence in map(str.rstrip, sys.stdin):
        print(
            '... {}'.format(convert.convert(sentence))
        )
        print('>>> ', end='', flush=True)


main()
