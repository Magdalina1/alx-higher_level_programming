#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


import sys


total_file_size = 0
status_codes = {}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        ip_address, _, _, _, status_code, file_size = line.split(' ')[0:6]
        total_file_size += int(file_size)
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_codes.keys()):
                print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    pass

print(f"Total file size: {total_file_size}")
for code in sorted(status_codes.keys()):
    print(f"{code}: {status_codes[code]}")
