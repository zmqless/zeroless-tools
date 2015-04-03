import argparse

from zeroless import Server
from .helpers import add_sub_commands, run_forever

def get_parser():
    parser = argparse.ArgumentParser(prog='Zeroless Server Cli',
                                     description='',
                                     epilog='')

    add_sub_commands(parser)
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    server = Server(port=args.port)

    run_forever(args, server)