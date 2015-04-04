import sys

def read_and_print(receiver, num_parts=1):
    for i in range(num_parts):
        data = next(receiver)

        if isinstance(data, bytes):
            print(data.decode("utf-8"))
        else:
            for part in data:
                print(str(data))

def wait_and_write(sender, num_parts):
    for i in range(num_parts):
        data = input().encode()
        sender(data)

def pub(socket, args):
    sender = socket.pub(topic=args.topic)

    while True:
        wait_and_write(sender, args.numParts)

def sub(socket, args):
    receiver = socket.sub(topics=args.topics)

    while True:
        read_and_print(receiver)

def push(socket, args):
    sender = socket.push()

    while True:
        wait_and_write(sender, args.numParts)

def pull(socket, args):
    receiver = socket.pull()

    while True:
        read_and_print(receiver)

def req(socket, args):
    sender, receiver = socket.request()

    while True:
        wait_and_write(sender, args.numParts)
        read_and_print(receiver)

def rep(socket, args):
    sender, receiver = socket.reply()

    while True:
        read_and_print(receiver)
        wait_and_write(sender, args.numParts)

def read_only_pair(socket, args):
    _, receiver = socket.pair()

    while True:
        read_and_print(receiver)

def write_only_pair(socket, args):
    sender, _ = socket.pair()

    while True:
        wait_and_write(sender, args.numParts)

def add_sender_command(subparser, name, callback):
    subparser = subparser.add_parser(name)
    subparser.add_argument('-n', '--numParts', type=int, default=1)
    subparser.set_defaults(run=callback)
    return subparser

def add_receiver_command(subparser, name, callback):
    subparser = subparser.add_parser(name)
    subparser.set_defaults(run=callback)
    return subparser

def add_sub_commands(parser):
    parser.add_argument('port', action='store', type=int,
                        choices=range(1024,65535), metavar="[a port between 1024 and 65535]",
                        help='an open port in the provided IP')

    subparsers = parser.add_subparsers(title='pattern',
                                       description='available pattern')

    parser_pub = add_sender_command(subparsers, 'pub', pub)
    parser_pub.add_argument('-t', '--topic', type=bytes, default=b'')

    parser_sub = add_receiver_command(subparsers, 'sub', sub)
    parser_sub.add_argument('-t', '--topics', type=list, default=[b''])

    parser_push = add_sender_command(subparsers, 'push', push)
    parser_pull = add_receiver_command(subparsers, 'pull', pull)
    parser_req = add_sender_command(subparsers, 'req', req)
    parser_rep = add_receiver_command(subparsers, 'rep', rep)

    parser_pair = subparsers.add_parser('pair')
    pair_subparsers = parser_pair.add_subparsers(title='pattern',
                                       description='available pattern')

    parser_write_only_pair = add_sender_command(pair_subparsers,
                                                'write-only',
                                                write_only_pair)

    parser_read_only_pair = add_receiver_command(pair_subparsers,
                                                 'read-only',
                                                 read_only_pair)

def run_forever(args, socket):
    try:
        args.run(socket, args)
    except EOFError:
        sys.exit()
    except KeyboardInterrupt:
        print()
        print('You pressed Ctrl+C!')
        sys.exit()