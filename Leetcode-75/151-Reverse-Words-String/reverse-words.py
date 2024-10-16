# PROBLEM #151 - REVERSE WORDS IN A STRING

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. 
# Do not include any extra spaces. --> Strip additional whitespace from beginning and end of input

#---------------------------------------------------------------------------------------------------------------------------

# INITIAL THOUGHTS:

# Iterate through the string --> Strings are immutable so we'd need a new string to populate the words
# The words should be added to the front of the string when encountered --> Build a stack?
# If we use an array and a stack, we can join the stack to return the resulting string?

# What if we just split the words by the white space --> Gives us an array of all words
# Then we simply need to reverse the array and rejoin all the words with a singular space
# Time would be O(n) --> Reversing the Array
# Space would be O(n) --> Size of Array needed to store words

#---------------------------------------------------------------------------------------------------------------------------


def reverseWords(s: str) -> str:
    words = s.split() # By splitting on the whitespace, we also then remove the leading and trailing white space
    
    print(words)
    
    words = words[::-1] # Reverses the array in python --> Puts our words in reversed order
    
    print(words)
    print(' '.join(words))

    return ' '.join(words) # Joins the words array by spaces and returns

reverseWords("      hello world")
reverseWords('Angelo is name My')