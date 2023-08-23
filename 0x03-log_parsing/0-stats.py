#!/usr/bin/env python3
"""parse that log"""
import sys
import signal

# Initialize variables to store statistics
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Define a function to print statistics"""
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
    print()


def signal_handler(signal, frame):
    """Define a signal handler to catch KeyboardInterrupt (CTRL + C)"""
    print_statistics()
    sys.exit(0)


# Set the signal handler for KeyboardInterrupt
signal.signal(signal.SIGINT, signal_handler)

# Process input from stdin line by line
for line in sys.stdin:
    line = line.strip()
    parts = line.split()

    # Check if the line has the correct format
    if len(parts) != 10:
        continue

    ip, _, _, _, _, status_code, file_size = parts
    try:
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue

    # Update statistics
    total_file_size += file_size
    if status_code in status_codes:
        status_codes[status_code] += 1

    line_count += 1

    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_statistics()
