#!/usr/bin/python3
""" reads stdin line by line and computes metrics"""


import Sys


def print_metrics(lines, total_size, status_codes):
    print("Total file size: File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(code + ": " + str(status_codes[code]))


try:
    lines = []
    total_size = 0
    status_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    for i, line in enumerate(sys.stdin):
        lines.append(line.strip())
        total_size += int(line.strip().split()[-1])
        if (i + 1) % 10 == 0:
            print_metrics(lines, total_size, status_codes)
except KeyboardInterrupt:
    print_metrics(lines, total_size, status_codes)
