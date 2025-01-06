# PROBLEM #1769 - MINIMUM NUMBER OF OPERATIONS TO MOVE ALL BALLS TO EACH BOX

# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.

# ---------------------------------------------------------------------------------------------------------------------------

# BRUTE FORCE SOLUTION

# As we move through the boxes string, we check the cost of moving each item into the current place
# Being that the constraint in the problem is 2000, this solution does pass but would be very inefficient - O(n^2) from the nested loops of the same string
# - To note, this was my first attempt at the solution as well


def minOperationsBrute(boxes: str) -> list[int]:
    # Create a result array that is used to store the value of total moves necessary for each index of boxes
    res = [0] * len(boxes)

    # Initial loop to move through each index of the string --> No need to convert as we are returning a separate array entirely
    for i in range(len(boxes)):

        # If the current box has a ball in it ('1' value), we iterate through all of the other boxes
        if boxes[i] == "1":

            # Second loop to iterate through all of the boxes while keeping our position in the current box (i)
            for j in range(len(boxes)):

                # For each box, we calculate the distance to the current box (j - i), we then add this answer to the position in the result array
                res[j] += abs(j - i)

                print(f"Resul Arr (Inner Loop): {res}")

    return res


# ---------------------------------------------------------------------------------------------------------------------------

# TWO POINTER ITERATIVE SOLUTION

# We use left and right pointers to track the total number of balls and moves on either side of each index.
# For each index, the left pointer tracks the total balls and moves accumulated from the left, while the right pointer does the same from the right.
# As we iterate through the string, we dynamically update the moves required for all balls on each side to reach the current index.
# The pointers traverse inward from both ends, ensuring that every index has the correct total moves calculated in a single pass.


def minOperations(boxes: str) -> list[int]:
    # Create a result array that is used to store the value of total moves necessary for each index of boxes
    res = [0] * len(boxes)

    # Create four variables (Ones for the left side of our index and ones for the right side)
    # - leftBalls and leftMoves represent the total balls encountered thus far and the total moves necessary to move those balls from the left to the current index
    # - rightBalls and rightMoves represent the same entities but for moving from the right side of the current index
    leftBalls, leftMoves = 0, 0
    rightBalls, rightMoves = 0, 0

    print(f"Before Loop: {res}")

    # Now we have a singular loop through the string --> Rather than the nested loops above (O(n^2))
    for i in range(len(boxes)):

        # We add the current moves from the left to the result array for this index
        res[i] += leftMoves

        # Then update the total balls encountered by adding the balls from the current box
        leftBalls += int(boxes[i])

        # Then update the total moves from the left, we add the leftBalls because this accounts for the move required for the next balls
        leftMoves += leftBalls

        print(f"Left Moves: {res}")
        print(f"Left Balls: {leftBalls}")

        # Initialize J to represent the right position in correlation to our current i index
        # - The end of the array - i positions --> As we iterate through the range, we will move this pointer inward from the right to the left
        j = (len(boxes) - 1) - i

        # Now we mirror the same actions performed for our left pointer but from the right side
        res[j] += rightMoves
        rightBalls += int(boxes[j])
        rightMoves += rightBalls

        print(f"Right Moves: {res}")
        print(f"Right Balls: {rightBalls}")

    print(f"Completed Res: {res}")
    return res


# From our print statements above, we can see how the result array is populated with the inclusive total moves as we iterate through the string
# - Notice how the index at 1 and len(boxes) - 2 are updated first, as there are no corresponding left or right moves at that point
# - As we iterate, we being to fill the total moves from each direction to the center of the array
# - Once our pointers overlap, we know we have updated with the total value from the right and the left moves

# minOperationsBrute("11011010101010101");

minOperations("11011010101010101")
# Result: [74, 66, 60, 54, 50, 48, 46, 46, 46, 48, 50, 54, 58, 64, 70, 78, 86]
