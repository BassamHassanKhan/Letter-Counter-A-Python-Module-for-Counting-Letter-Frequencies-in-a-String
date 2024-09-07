
"""
This module provides a function to count the occurrences of each letter in a given string.

Functions:
    LetterCounter(text): Returns a dictionary with the count of each letter in the input string.

Acknowledgments:
    This code is a collaborative effort of multiple contributors.

Usage example:
    result = LetterCounter("mathematics")
    print(result)  # Output: {'m': 2, 'a': 2, 't': 2, 'h': 1, 'e': 1, 'i': 1, 'c': 1, 's': 1}


"""

def LetterCounter(list):
    dict = {}
    for letter in list:
        if letter not  in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict


list = "mathematics"
output = LetterCounter(list)
print(output)
