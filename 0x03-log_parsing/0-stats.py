#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define the regular expression for parsing log lines
log_regex = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

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
try:
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
except KeyboardInterrupt:
    # Print summary when interrupted by keyboard (CTRL + C)
    print_summary()
    sys.exit(0)

# Print final summary when the input ends
print_summary()
