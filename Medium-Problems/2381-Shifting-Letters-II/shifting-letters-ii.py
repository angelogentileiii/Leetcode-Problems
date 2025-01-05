# PROBLEM 2381 - SHIFTING LETTERS II

# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]
# For every i, shift the characters in s from the index start[i] to the index end[i] (inclusive)
# --> Forward if direction[i] = 1, or shift the characters backward if direction[i] = 0

# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a')
# Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z')

# Return the final string after all such shifts to s are applied

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# PREFIX SUM TECHNIQUE
# Similar to problem #2559 -> Calculate all of the shifts possible BEFORE performaing the shifts
# If we shift for each index of the shifts array, it can become a very slow process --> My first solution failed on Leetcode because of this

# ---------------------------------------------------------------------------------------------------------------------------


def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
    # Initialize an array to keep track of the cumulative shift directions
    # The extra element (len(s) + 1) is added to help manage shifts at the end of the string
    # This ensures that we don't modify the array beyond the last character, avoiding index errors
    moves = [0] * (len(s) + 1)

    # Print the initial moves array to track the shifts
    print(f"Shift Arr: {moves}")

    # Iterate through each shift in the shifts list
    # Each shift contains [start, end, direction], where:
    # - start: starting index for the shift
    # - end: ending index for the shift
    # - direction: 1 for right shift, -1 for left shift
    for shift in shifts:
        start, end, direction = shift

        # Increment or decrement the shift at the start index based on the direction
        moves[start] += 1 if direction == 1 else -1

        # If the end index + 1 is within the bounds of the string,
        # adjust the shift at end + 1 to mark the end of the current shift range
        if end + 1 < len(s):
            moves[end + 1] -= 1 if direction == 1 else -1

        # Print the moves array after processing the current shift to track the updates
        print(f"After Processing Shift: {moves}")

    # Initialize a variable to accumulate the current shift at each index
    curr_shift = 0

    # Convert the string `s` to a list to allow mutable operations (strings are immutable)
    s = list(s)

    # Iterate through each character in the string to apply the calculated shifts
    for i in range(len(s)):
        # Accumulate the shift at the current index
        curr_shift += moves[i]

        # Print the cumulative shift for the current character index
        print(f"Curr Shift: {curr_shift}")

        # Calculate the net shift for the current character, ensuring it stays within the range [0, 25]
        # This is done by using modulo 26. Adding 26 ensures that negative shifts are handled correctly
        net_shift = ((curr_shift % 26) + 26) % 26

        # Print the calculated net shift for debugging purposes
        print(f"Net Shift: {net_shift}")

        # Calculate the new character after applying the net shift
        # We convert the current character to its zero-indexed position by subtracting the ASCII value of 'a'
        # Then, we add the net shift, use modulo 26 to handle wraparound, and convert back to the correct character
        # The final result is the new character after the shift
        print(
            f'Letter Shifted: {s[i]} to {chr((ord(s[i]) - ord("a") + net_shift) % 26 + ord("a"))}'
        )

        # Update the character in the list with the shifted character
        s[i] = chr((ord(s[i]) - ord("a") + net_shift) % 26 + ord("a"))

    # Print the final string after all shifts have been applied
    print(f'Completed String: {"".join(s)}')

    # Join the list back into a string and return the final result
    return "".join(s)


# ---------------------------------------------------------------------------------------------------------------------------

shiftingLetters(
    "abc",
    [
        [0, 1, 0],
        [1, 2, 1],
        [0, 2, 1],
    ],
)

shiftingLetters(
    "dztz",
    [
        [0, 0, 0],
        [1, 1, 1],
    ],
)
