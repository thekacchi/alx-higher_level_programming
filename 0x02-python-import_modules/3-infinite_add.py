#!/usr/bin/python3

import sys


def main():
    count = len(sys.argv) - 1
    if count == 0:
        print(0)
    elif count > 0:
        summ = 0
        i = 1
        for i in range(count):
            asum = sys.argv[i + 1]
            summ = summ + int(asum)
            i = i + 1

        print(summ)


if __name__ == "__main__":
    main()
