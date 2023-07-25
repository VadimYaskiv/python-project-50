import argparse


def parse_line():
    parser = argparse.ArgumentParser(description='Compares two\
            configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        choices=['stylish', 'plain', 'json'],
                        nargs='?',
                        default='stylish', type=str,
                        help='set format of output')

    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    format = args.format
    return first_file, second_file, format
