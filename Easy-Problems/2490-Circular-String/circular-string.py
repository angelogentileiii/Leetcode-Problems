# PROBLEM 2490 - CIRCULAR STRING

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

# A sentence is circular if:

# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences.
# However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

# Given a string sentence, return true if it is circular. Otherwise, return false.

# ---------------------------------------------------------------------------------------------------------------------------

# CAN USE NEGATIVE INDEXING IN PYTHON --> DON'T FORGET!
# Can also use len(item) - 1 as well....


def isCircularSentence(sentence: str) -> bool:
    # Split the sentence into an array
    sen_arr = sentence.split()

    # Grab the first word
    first_word = sen_arr[0]

    # Grad the last word
    last_word = sen_arr[-1]

    # Compare the first letter of the first word to the last letter of the last work
    if first_word[0] != last_word[-1]:
        return False

    # Compare each word to the prior word --> Beginning at the second word in array
    for i in range(1, len(sen_arr)):
        # First character of current word compared to last character of prior word
        if sen_arr[i][0] != sen_arr[i - 1][-1]:
            return False

    return True


print(isCircularSentence("leetcode exercises sound delightful"))
print(isCircularSentence("ab a"))
