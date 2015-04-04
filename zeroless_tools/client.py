import argparse

from zeroless import Client
from .helpers import add_sub_commands, run_forever

def get_parser():
    parser = argparse.ArgumentParser(prog='Zeroless Client Cli',
                                     description='',
                                     epilog='')
    parser.add_argument('-i', '--ip', action='store', type=str,
                        default='127.0.0.1',
                        help='an IP to connect to')

    add_sub_commands(parser)
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    client = Client()
    client.connect(args.ip, args.port)

    run_forever(args, client)