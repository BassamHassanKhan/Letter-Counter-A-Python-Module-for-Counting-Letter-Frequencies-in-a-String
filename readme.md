# Letter Counter: A Python Module for Counting Letter Frequencies in a String

This Python module provides a simple function to count the occurrences of each letter in a given string. It can be useful for text analysis or any situation where you need to analyze letter frequencies.

## Features:
- Count occurrences of each letter in a string.
- Lightweight and easy to integrate into other Python projects.
- Supports any string input.

## Usage

### Function: `LetterCounter(text)`
Returns a dictionary with the count of each letter in the input string.

### Example:

```python
from letter_counter import LetterCounter

text = "mathematics"
result = LetterCounter(text)
print(result)  # Output: {'m': 2, 'a': 2, 't': 2, 'h': 1, 'e': 1, 'i': 1, 'c': 1, 's': 1}
