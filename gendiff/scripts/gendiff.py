#!/usr/bin/env python3
import argparse
import json
from gendiff.code.comparison import compare_dict


def main():
    parser = argparse.ArgumentParser(description='Compares two\
            configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()

    with (open(args.first_file, 'r') as file1,
          open(args.second_file, 'r') as file2):
        json1 = json.load(file1)
        json2 = json.load(file2)

    print(compare_dict(json1, json2))


if __name__ == '__main__':
    main()
