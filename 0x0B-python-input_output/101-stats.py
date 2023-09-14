#!/usr/bin/python3
"""This module is defining a function"""
import sys


def print_metrics(total_size, status_coses):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    line_count = 0
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) >= 2:
                status_code = int(parts[-2])
                total_size += int(parts[-1])
                if status_code in status_codes:

                    status_codes[status_code] += 1
            line_count += 1
        except ValueError:
            pass

        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
