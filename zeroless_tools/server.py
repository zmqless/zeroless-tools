import sys
import argparse

from zeroless import Server
from .helpers import (add_sub_commands, run)

def get_parser():
    parser = argparse.ArgumentParser(prog='Zeroless Server Cli',
                                     description='',
                                     epilog='')

    add_sub_commands(parser)
    return parser

def zeroserver(args):
    parser = get_parser()
    parsed_args = parser.parse_args(args)
    server = Server(port=parsed_args.port)
    socket_executor = parsed_args.socket_executor(server, parsed_args)

    return socket_executor

def main(args=sys.argv[1:]):
    socket_executor = zeroserver(args)

    while True:
        run(socket_executor)