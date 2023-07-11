#!/usr/bin/python3
""" reads stdin line by line and computes metrics"""


def print_metrics(lines, total_size, status_codes):
    print("Total file size: File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(code + ": " + str(status_codes[code]))


try:
    lines = []
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403":
                    0, "404": 0, "405": 0, "500": 0}
    for i, line in enumerate(iter(input, '')):
        lines.append(line.strip())
        total_size += int(line.strip().split()[-1])
        if (i + 1) % 10 == 0:
            print_metrics(lines, total_size, status_codes)
except KeyboardInterrupt:
    print_metrics(lines, total_size, status_codes)
