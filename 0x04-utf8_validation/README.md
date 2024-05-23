# UTF-8 Validation

## Overview

This project involves writing a Python function that determines if a given data set represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding that can use 1 to 4 bytes for each character.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS

## Usage

### Function Prototype

```python
def validUTF8(data)
```

- **Parameters:**
  - `data`: A list of integers representing the data, where each integer is a byte.
- **Returns:**
  - `True` if the data set is a valid UTF-8 encoding.
  - `False` otherwise.

### Example Usage

Create a file named `0-main.py`:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Expected output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Expected output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Expected output: False
```

### Running the Tests

Make the script executable and run it:

```bash
chmod +x 0-main.py
./0-main.py
```

## Project Structure

- `0-validate_utf8.py`: Contains the implementation of the `validUTF8` function.
- `0-main.py`: Main file for testing the `validUTF8` function.

## Implementation Details

The `validUTF8` function works by:
1. Checking if each integer in the list is a valid byte (0-255).
2. Determining the number of bytes in the current UTF-8 character based on the leading bits of the first byte.
3. Validating that subsequent bytes in the multi-byte sequence follow the `10xxxxxx` pattern.

### Bitwise Operations Used

- `mask1 = 1 << 7` to check the most significant bit (10000000).
- `mask2 = 1 << 6` to check the second most significant bit (01000000).

## Author

Muna Said

## License

This project is licensed under the MIT License.
