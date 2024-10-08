# Problem #2696 --> MINIMUM STRING LENGTH AFTER REMOVING SUBSTRINGS

# You are given a string s consisting only of uppercase English letters.

# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

# Return the minimum possible length of the resulting string that you can obtain.

# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

#---------------------------------------------------------------------------------------------------------------------------

# Utilize a data structure to keep track of characters and in order visited
    # a stack --> pop the last element added to the list
    # if string is "ABCBBA":
        # stack we would pop() the last item if we encounted the condition (LIFO)

#---------------------------------------------------------------------------------------------------------------------------
    
# STACK SOLUTION
def minLength(s: str) -> int:
    stack = []

    # for char in s:
    #     # Only actually need to check for letter 'B' and 'D' then check if character in front is one of two
    #     if char == 'B':
    #         # When we find a 'B', we check if the last element in the stack is an 'A' or a 'B'
    #         # If it matches the condition, we remove that item from the stack and move to next iteration
    #         if stack and stack[len(stack) - 1] == 'A':
    #             stack.pop()
    #         else:
    #             # If it is not, we add the character 'B' to the stack
    #             stack.append(char)
    #     elif char == 'D':
    #         if stack and stack[len(stack) - 1] == 'C':
    #             stack.pop()
    #         else:
    #             stack.append(char)
    #     else:
    #         stack.append(char) # If it doesn't match, it is a character we keep, push into stack

    # MAXIMUM READABILITY
    for char in s:
        cond1 = char == 'B' and stack and stack[-1] == 'A'
        cond2 = char == 'D' and stack and stack[-1] == 'C'

        stack.pop() if cond1 or cond2 else stack.append(char)

    return len(stack)

# TWO-POINTER SOLUTION
def minLength2(s: str) -> int:
    chars = list(s)
    index = 0

    # for i in range(len(chars)):
    #     if index > 0 and chars[i] == 'B':
    #         if chars[i-1] == 'A':
    #             index -= 1
    #         else:
    #             chars[index] = chars[i]
    #             index += 1
    #     elif index > 0 and chars[i] == 'D':
    #         if chars[i-1] == 'C':
    #             index -= 1
    #         else:
    #             chars[index] = chars[i]
    #             index += 1
    #     else:
    #         chars[index] = chars[i]
    #         index += 1

    # MATCH/CASE STATEMENT INSTEAD
    for i in range(len(chars)):
        match chars[i]:
            case 'B':
                if index > 0 and chars[index-1] == 'A':
                    index -= 1
                else:
                    chars[index] = chars[i]
                    index += 1
            case 'D':
                if index > 0 and chars[index-1] == 'C':
                    index -= 1
                else:
                    chars[index] = chars[i]
                    index += 1
            case _:
                chars[index] = chars[i]
                index += 1

    return index



minSeq1 = 'ABBCDACBABCDE' # Answer expected is 5
minSeq2 = 'ABBBABBAB' # Answer expected is 3

print('Answer #1: ', minLength(minSeq1))
print('Answer #2: ', minLength(minSeq2))
