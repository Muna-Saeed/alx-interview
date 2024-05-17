# 0x03. Log Parsing

---

# 0x03. Log Parsing

## Description

This project involves parsing and processing log data in real-time. The goal is to read log entries from standard input, extract relevant information, and compute metrics such as the total file size and the number of occurrences of each HTTP status code. The script prints these statistics after every 10 lines of input and when interrupted by a keyboard signal (CTRL + C).

## Requirements

- Python 3.4.3 or later
- The script should be executable.
- The script should handle keyboard interruptions gracefully and print a summary of the collected data.

## Concepts Needed

To successfully complete this project, you should be familiar with the following concepts:

### File I/O in Python

- Reading from `sys.stdin` line by line.
- Input and output operations in Python.

### Signal Handling in Python

- Handling keyboard interruption (CTRL + C) using signal handling in Python.
- Utilizing the `signal` module in Python.

### Data Processing

- Parsing strings to extract specific data points.
- Aggregating data to compute summaries.

### Regular Expressions

- Using regular expressions to validate the format of each line.
- The `re` module in Python for working with regular expressions.

### Dictionaries in Python

- Using dictionaries to count occurrences of status codes and accumulate file sizes.
- Understanding dictionary methods and operations.

### Exception Handling

- Handling possible exceptions that may arise during file reading and data processing.
- Utilizing `try`, `except`, and `finally` blocks for exception handling.

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

## Project Structure

- `0-generator.py`: A script that generates log entries and writes them to standard output. This script is used to simulate log data.
- `0-stats.py`: The main log parsing script that reads from standard input, processes the log data, and prints the statistics.

## How to Use

### Running the Log Generator

First, ensure `0-generator.py` is executable. You can make it executable by running:

```bash
chmod +x 0-generator.py
```

Run the log generator script:

```bash
./0-generator.py
```

### Running the Log Parsing Script

Similarly, ensure `0-stats.py` is executable:

```bash
chmod +x 0-stats.py
```

Run the log parsing script. You can pipe the output of `0-generator.py` to `0-stats.py`:

```bash
./0-generator.py | ./0-stats.py
```

### Example Output

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
```

## Script Details

### 0-generator.py

This script generates log entries in the following format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

- IP Address: Randomly generated
- Date: Current date and time
- Status Code: Randomly chosen from a set of possible values (200, 301, 400, 401, 403, 404, 405, 500)
- File Size: Randomly generated between 1 and 1024

### 0-stats.py

This script reads from standard input and processes log entries in real-time. It performs the following tasks:

1. Reads lines from standard input.
2. Matches each line against a predefined regular expression to extract the status code and file size.
3. Updates counters for the total file size and the number of occurrences of each status code.
4. Prints the statistics after every 10 lines and upon receiving a keyboard interruption (CTRL + C).

#### Key Functions and Variables

- **Regular Expression**: Used to parse log lines.
- **Counters**: Track the total file size and the number of occurrences of each status code.
- **print_summary()**: Prints the current statistics.

## Handling Interruptions

The script uses signal handling to ensure that when interrupted by a keyboard signal (CTRL + C), it prints the final summary before exiting.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
