# Vowel Count
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, and u as vowels for this Kata.

# The input string will only consist of lower case letters and/or spaces.

input = 'abdcdefehik'

def vowel_count(word):
    return sum(1 for letter in word if letter in ('aeouiAEOUI'))


print(vowel_count(input))