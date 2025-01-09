# PROBLEM #2185 - COUNTING WORDS WITH A GIVEN PREFIX

# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.

# ---------------------------------------------------------------------------------------------------------------------------


def prefixCount(words: list[str], prefix: str) -> int:
    # Initialize our count variable --> Will output total words with prefix
    count = 0

    for word in words:
        # Option #1: Slice the word from the beginning to the length of the prefix --> Check if the sliced string and the prefix match
        # if (word[:len(prefix)] == prefix): count += 1

        # Option #2: Utilize built in method to determine if word begins with the prefix
        if word.startswith(prefix):
            count += 1

    print(f"Result: {count}")
    return count


prefixCount(["pay", "attention", "practice", "attend"], "at")
