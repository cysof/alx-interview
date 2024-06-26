def validUTF8(data):
  """
  Determines if a given data set represents a valid UTF-8 encoding.

  Args:
      data: A list of integers representing bytes of data.

  Returns:
      True if data is a valid UTF-8 encoding, else return False.
  """
  count_ones = 0
  for num in data:
    # Extract the 8 least significant bits
    num = num & 0xFF
    if count_ones == 0:
      # First byte of a character
      if num >= 0xC2 and num <= 0xF4:
        count_ones = 1
      elif num == 0xC0 or num == 0xC1:
        count_ones = 2
      elif num >= 0xF5:
        return False
      else:
        # Valid single-byte ASCII character
        count_ones = 0
    else:
      # Subsequent bytes of a character
      if num >= 0x80 and num <= 0xBF:
        count_ones -= 1
      else:
        return False
  return count_ones == 0