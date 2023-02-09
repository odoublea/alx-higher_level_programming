#!/usr/bin/python3

import sys

"""Log parsing module"""


def parse_line(line):
    """Parse a line of input into a tuple of (status code, file size)"""
    parts = line.strip().split()
    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return (status_code, file_size)

# Initialize the counters


total_size = 0
status_counts = {code: 0 for code in (200, 301, 400, 401, 403, 404, 405, 500)}


def print_statistics():
    """Print the current statistics"""
    print("Total file size: File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print("{}: {}".format(status_code, count))


# Read lines from stdin and process them
try:
    line_number = 0
    for line in sys.stdin:
        line_number += 1
        status_code, file_size = parse_line(line)
        total_size += file_size
        status_counts[status_code] += 1

        # Print the statistics after every 10 lines or if interrupted
        if line_number % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
