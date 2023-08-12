#!/usr/bin/python3

import sys


def main():
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(count))
        s_num = 1
        for arg in range(count):
            print("{}: {}".format(s_num, sys.argv[arg + 1]))
            s_num = s_num + 1


if __name__ == "__main__":
    main()
