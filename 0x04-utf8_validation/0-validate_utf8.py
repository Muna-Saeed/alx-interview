#!/usr/bin/python3
"""
Function to determine if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the data represents a valid UTF-8 encoding.
    :param data: List of integers representing the data
    :return: True if valid UTF-8 encoding, False otherwise
    """
    
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Loop through each integer in the data list
    for num in data:
        
        # Ensure num is within a byte range (0-255)
        if num > 255:
            return False
        
        # If num_bytes is zero, we need to start a new UTF-8 character
        if num_bytes == 0:
            # Count the number of leading 1s in the first byte
            mask = 1 << 7
            while mask & num:
                num_bytes += 1
                mask = mask >> 1
            
            # 1-byte characters (0xxxxxxx) or invalid 0xxxxxx
            if num_bytes == 0:
                continue
            
            # If the number of bytes is more than 4 or is 1 (which is invalid in UTF-8)
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the num is of the form 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False
        
        # Decrement the number of bytes to process
        num_bytes -= 1
    
    # If we finish processing and have processed all bytes correctly
    return num_bytes == 0
