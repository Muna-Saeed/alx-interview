# UTF-8 Validation

## Overview

This project involves writing a Python function that determines if a given data set represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding that can use 1 to 4 bytes for each character.

For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here’s a list of concepts and resources that will be helpful:

### Concepts Needed:

#### Bitwise Operations in Python:
- Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).
- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)

#### UTF-8 Encoding Scheme:
- Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
- Understanding the patterns that represent a valid UTF-8 encoded character.
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/characters-vs-bytes/)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

#### Data Representation:
- How to represent and work with data at the byte level.
- Handling the least significant bits (LSB) of integers to simulate byte data.

#### List Manipulation in Python:
- Iterating through lists, accessing list elements, and understanding list comprehensions.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

#### Boolean Logic:
- Applying logical operations to make decisions within the program.

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

### Additional Resource:
- [Mock Technical Interview](https://www.pramp.com/)

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
