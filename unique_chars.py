"""
PROBLEM:
  Input: string, Output: boolean
  Return true if all chars in string are unique, false if we have repeats
EXAMPLE:
  unique_chars('abcd') -> True
  unique_chars('abbb') -> False
  unique_chars('AaBbCc') -> True
  unique_chars('') -> None
DATA STRUCTURE:
  - Dictionary
  - List
ALGORITHM:
  0. string length == 0 ? return None
  1. create list of chars (split)
  2. iterate over list of chars
    1. if char already a key
      return false
    2. if char not a key, set as key
  3. return True
"""
def unique_chars(phrase):
    char_counter = {}
    if len(phrase) == 0:
        return None
    for char in phrase:
        if char in char_counter:
            return False
        char_counter[char] = 1
    return True

# Tests
print(unique_chars('abc'), 'true')
print(unique_chars('abbb'), 'false')
print(unique_chars('AbCc'), 'true')
print(unique_chars(''), 'none')