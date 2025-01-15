# PROBLEM #2429 - MINIMIZE XOR

# Given two positive integers num1 and num2, find the positive integer x such that:
#   - x has the same number of set bits as num2, and
#   - The value x XOR num1 is minimal.

# Note that XOR is the bitwise XOR operation.

# Return the integer x. The test cases are generated such that x is uniquely determined.

# The number of set bits of an integer is the number of 1's in its binary representation.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# Bit wise operations mean utilizing the binary code version of the integer ('0101') to calculate values
# This problem wants us to modify num1 to have the same number of 1 bits in our binary code as num2
#   - While also keeping num1 as small as possible as an integer

# XOR means 'Exclusive OR'
#   - A logical operation that compares two binary bits. The result of XOR is:
#       - 1 if the bits are different (one is 1 and the other is 0).
#       - 0 if the bits are the same (both are 0 or both are 1).
#  - If we compare 3 ('011') and 5 ('101') --> We get the number 6 ('110')
#       - First and second bits are different (return 1) but final bit is the same (return 0)

# By determining the number of bits in each num then increasing or decreasing num1 acccordingly,
# we ensure that we are only performing the minimum operations to complete our solution
#   - Indirectly fulfilling the condition of x XOR num1 is minimal

# ---------------------------------------------------------------------------------------------------------------------------


def minimizeXor(num1: int, num2: int) -> int:
    # Python has a built in bit_count method --> Other languages may not have such
    # Count the '1' bits within num1 and store in variable
    num1Bits = num1.bit_count()
    print(f"Bits in Num1: {num1Bits}")

    # Perform the same '1' bit counting for num2
    num2Bits = num2.bit_count()
    print(f"Bits in Num2: {num2Bits}")

    # If our num1 has more '1' bits than num2 --> We need to reduce the number of '1' bits in num1
    while num1Bits > num2Bits:
        # num1 - 1 will 'turn off' the rightmost bit in num1 --> 6('110') becomes 5('101')
        # the '&=' (bitwise AND) operator clears the rightmost bit --> 6 & 5 = 4 ('100')
        #   - Will only set the bits of num1 to '1' if the right hand side (num1 - 1) also has '1' bits in the same position
        num1 &= num1 - 1

        # Since we have removed a '1' bit, we need to update our num1Bits accordingly --> Can do so without reusing bit_count since we know we decreased by 1
        num1Bits -= 1

        print(f"Updated num1 Val: {num1} - '1' Bits: {num1Bits}")

    # Perform the inverse actions for the condition --> If num1 has more '1' bits than num2
    while num1Bits < num2Bits:
        # num + 1 would flip the rightmost bit from 0 to 1 or from 1 to 0 and bubble up a new '1' bit --> 7('111') becomes 8('1000')
        # the '|=' (bitwise OR) operator sets a bit to '1' if either the left or right number have a '1' bit in that space
        #   - So if we have 5 ('101') | 6 ('110'), we would get 7 ('111') because each space has a '1' bit in either of the two numbers
        num1 |= num1 + 1

        # Now that we have increased the 1 bits in our number, we must also increase the value in our variable
        num1Bits += 1

        print(f"Updated num1 Val: {num1} - '1' Bits: {num1Bits}")

    print(f"Final Updated Number: {num1}\n")
    return num1


# View the print statements to see how we fulfill x XOR num1 --> We make the minimum amount of changes necessary to equalize our '1' bits

minimizeXor(8, 7)
minimizeXor(127, 8)
