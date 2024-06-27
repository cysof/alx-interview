#!/usr/bin/python3

""" UTF-8 Validation
Python script that determines is a given data set
represents a valid UTF-8 encoding.
Return True if valid, False otherwise.
Data set can contain multiple characters.
Data will be represented by a list of integers.
"""


def validUTF8(data):
    """ Determine if a given data set represents a valid UTF-8 encoding.
      For each byte:
      If num_bytes is 0, it means we're starting a new UTF-8 character.
      We need to determine how many bytes this character will have:
        If the byte starts with 110, it's a 2-byte character.
        If it starts with 1110, it's a 3-byte character.
        If it starts with 11110, it's a 4-byte character.
        If it starts with 0 (in the most significant bit),
          it's a single-byte character.
        If none of these conditions are met,
          it's an invalid UTF-8 byte sequence so we return False.
      If num_bytes is not 0, it means we're in the middle of a
        multi-byte character, and the current byte should start with 10.
      If it doesn't, it's invalid, so we return False.
      After processing each byte, if there are still bytes left in the
        current multi-byte character (i.e., num_bytes is not 0), it means the
        input data is incomplete and therefore invalid.
      If all bytes are processed without encountering any issues,
        and there are no trailing bytes from incomplete multi-byte characters,
        we return True, indicating that the input data
        is a valid UTF-8 encoding.
    """
    # number of bytes in current UTF-8 character
    num_bytes = 0

    # loop through each byte in data set
    for byte in data:
        # if this is start byte of the utf-8 character
        if num_bytes == 0:
            # determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:  # we check if it is not a continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    # if there are trailing bytes left in the data set, it's invalid
    return num_bytes == 0