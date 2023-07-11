#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


import sys


# Initialize variables
total_file_size = 0
status_codes = {}
line_count = 0

try:
    # Read input line by line
    for line in sys.stdin:
        line_count += 1

        # Process each line and update metrics
        _, _, _, _, status_code, file_size = line.strip().split(' ')[0:6]
        total_file_size += int(file_size)
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_codes.keys()):
                print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    pass

# Print the final statistics
print(f"Total file size: {total_file_size}")
for code in sorted(status_codes.keys()):
    print(f"{code}: {status_codes[code]}")
