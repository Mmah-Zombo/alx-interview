#!/usr/bin/python3
"""log that"""

import sys
import signal

# Initialize variables
total_file_size = 0
status_codes_count = {}


def signal_handler(sig, frame):
    """Handle keyboard interruption"""
    print_stats()
    sys.exit(0)


def print_stats():
    """Print the current statistics"""
    print("File size:", total_file_size)
    for status_code in sorted(status_codes_count):
        print(f"{status_code}: {status_codes_count[status_code]}")
    print()


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read input line by line
    for line_count, line in enumerate(sys.stdin, start=1):
        parts = line.split()

        # Check if the line format matches
        if len(parts) != 9 or parts[5][0] != '"' or not parts[8].isdigit():
            continue

        status_code = parts[7]
        file_size = int(parts[8])

        # Update total file size
        total_file_size += file_size

        # Update status codes count
        if status_code.isdigit():
            status_codes_count[status_code] = (status_codes_count
                                               .get(status_code, 0) + 1)

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

# Print final stats
print_stats()
