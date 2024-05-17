#!/usr/bin/python3
"""
Log parsing
a script that reads stdin line by line and computes metrics.
"""

import sys
import signal
import re


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

#log_regex = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

log_regex = re.compile(r"^(\S+)\s*-\s*\[.*?\] \"GET /projects/260 HTTP/1.1\" (\S+) (\d+)$")

def print_summary():
    """ Print the summary of log data """
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    """ Handle the signal to print summary """
    print_summary()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process input lines
for line in sys.stdin:
    line = line.strip()
    match = log_regex.match(line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))

        # Update total file size
        total_size += file_size

        # Update status code counts
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        # Print summary every 10 lines
        if line_count % 10 == 0:
            print_summary()

# Print final summary when the input ends
print_summary()
