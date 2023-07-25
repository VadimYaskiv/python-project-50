#!/usr/bin/env python3
from gendiff.comparison.gendiff_logic import generate_diff
from gendiff.comparison.line_parser import parse_line


def main():
    first_file, second_file, format = parse_line()
    print(generate_diff(first_file, second_file, format))


if __name__ == '__main__':
    main()
