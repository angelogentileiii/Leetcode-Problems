# PROBLEM #2182 - CONSTRUCT A STRING WITH A REPEAT LIMIT

# You are given a string s and an integer repeatLimit.
# Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row.
# You do not have to use all characters from s.

# Return the lexicographically largest repeatLimitedString possible.

# A string a is lexicographically larger than a string b if:
# In the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.
# If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# lexicographically larger means sorted from z to a --> Z > A but must maintain REPEAT LIMIT
# Sort list and get the characters in this proper order first

# Move through the list and add the characters to a result string as long as they are less than the repeat limit in frequency
# Return the string?

# ---------------------------------------------------------------------------------------------------------------------------


def repeatLimitedString(s: str, repeatLimit: int) -> str:
    # Sort the input string in reverse order --> Lexicographically largest first
    # Reverse = True ensures that we are sorted from Z to A
    chars = sorted(s, reverse=True)
    print(f"Lex Sorted: {chars}")

    # This variable will contain the characters for our final string to return --> In Lexagraphical order
    result = []

    # This variable represents the current count of the current character we are using --> Cannot exceed repeatLimit integer
    count = 0

    # This variable represents the index of the next available character to append to the result once we have reached our count limit
    point = 0

    # Initialize a loop to traverse through the sorted characters in chars
    for i in range(len(chars)):
        # Check if result is not empty and if the last character is the same as our current character
        if result and result[-1] == chars[i]:
            # Check the current count of that character
            if count < repeatLimit:
                # Add the character to the result and increase the count
                result.append(chars[i])
                count += 1
                point += 1
            else:
                # Move the pointer to the next distinct letter --> Only using i + 1 may have us revisit multiple copies of the same letter
                # Use max(point, i + 1) to avoid all duplicate characters more efficiently --> Times out with simply i + 1
                point = max(point, i + 1)

                # While loop where we skip over charaters that are the same as chars[i]
                # This helps us with the max function above, allowing us to skip to the next distinct character more efficiently
                # Continues until end of list or distinct character is found
                while point < len(chars) and chars[point] == chars[i]:
                    point += 1

                if point < len(chars):
                    # Append the viable character
                    result.append(chars[point])

                    print(
                        f"Before Swap: Chars[i] = {chars[i]}, Chars[Point] = {chars[point]}, Chars = {chars}"
                    )

                    # Switch our pointers to move i to the new distinct character
                    chars[i], chars[point] = chars[point], chars[i]

                    print(
                        f"After Swap: Chars[i] = {chars[i]}, Chars[Point] = {chars[point]}, Chars = {chars}"
                    )

                    count = 1

                else:
                    # Can add the break in because we know we cannot add anymore characters to the string
                    break

        else:
            # If the result is empty, we simply add the character and update the count
            result.append(chars[i])
            count = 1

    print(f"Result: {result}")
    print(" ")

    return "".join(result)


# ---------------------------------------------------------------------------------------------------------------------------

# THIS SOLUTION USES A PRIORITY QUEUE AND MAP TO TRACK THE CHARACTERS AND ADD INTO THE RESULT STRING

from heapq import heapify, heappop, heappush
from collections import Counter


def repeatLimitedStringHeap(s: str, repeatLimit: int) -> str:
    # Create a counter map to track each character and it's appearances within the string
    freq = Counter(s)
    print(f"FREQ: {freq}")

    # Create a priority queue (Minimum Heap)
    # --> Lexicographical order means the smallest should be at the top of the heap
    # --> ord returns the unicode point of each character so ord('a') - ord(char) is 0 - unicode point (ex: z would equal -25 --> Top of MinHeap)
    pq = [(ord("a") - ord(char), count) for char, count in freq.items()]
    heapify(pq)
    print(
        f"PQ: {pq} --> WITH CHAR: {[(chr(ord('a') - priority), count) for priority, count in pq]}"
    )

    # Empty result to store the characters for our completed string
    result: list[str] = []

    # Loop exists as long as there are elements within the priority queue
    while pq:
        # Pop the lexicographically largest element (smallest unicode) from the heap with it's count integer
        char, count = heappop(pq)
        print(f"CHAR AND COUNT: {(chr(ord('a') - char), count)}")

        # Find the maximum amount that character can be repeated in the result string --> Limited by frequency or by repeatLimit
        repeat = min(repeatLimit, count)
        print(f"Max Repeat: {repeat}")

        # Append that character as many times as the calculated maximum
        result.append(chr(ord("a") - char) * repeat)
        print(f"RESULT: {result}")

        # Reduce the count of that character by the amount that has been inserted into the result string
        count -= repeat
        print(f"UPDATE COUNT: {count}")

        # If there are still more of the same character available and the queue is not empty
        if count > 0 and pq:
            # We move to the next character by popping from the priority queue (the next lexicographically largest character and count)
            next_char, next_count = heappop(pq)
            print(f"NEXT CHAR AND COUNT: {(chr(ord('a') - next_char), next_count)}")

            # We append one of that character to the string
            result.append(chr(ord("a") - next_char))

            # If there are more of that character available, we push it into the heap with a reduced count
            if next_count > 1:
                heappush(pq, (next_char, next_count - 1))

            # Then we push our prior character into the heap with a reduced count as well
            heappush(pq, (char, count))

            # By doing the above, we are able to alternate between the largest lexicographical characters until they are dispersed properly
            print(
                f"CURRENT HEAP STATUS: {[(chr(ord('a') - priority), count) for priority, count in pq]}"
            )

        print(f"CURRENT ITERATION: {result}")

    print(f'ANSWER: {"".join(result)}')
    print(" ")

    # Join the result array and return the completed string
    return "".join(result)


repeatLimitedString("cczazcc", 3)

repeatLimitedString("aababab", 2)

print("-" * 35)

repeatLimitedStringHeap("cczazcc", 3)
repeatLimitedStringHeap("aababab", 2)
