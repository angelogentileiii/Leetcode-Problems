// PROBLEM #1769 - MINIMUM NUMBER OF OPERATIONS TO MOVE ALL BALLS TO EACH BOX

// You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

// In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

// Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

// Each answer[i] is calculated considering the initial state of the boxes.

// ---------------------------------------------------------------------------------------------------------------------------

// BRUTE FORCE SOLUTION

// As we move through the boxes string, we check the cost of moving each item into the current place
// Being that the constraint in the problem is 2000, this solution does pass but would be very inefficient - O(n^2) from the nested loops of the same string
// - To note, this was my first attempt at the solution as well

function minOperationsBrute(boxes: string): number[] {
    const n = boxes.length;
    let result = new Array(n).fill(0);

    console.log(`Empty Result Arr: ${result}`);

    for (let i = 0; i < n; i++) {
        if (boxes[i] === "1") {
            for (let j = 0; j < n; j++) {
                result[j] += Math.abs(j - i);
            }

            console.log(`Result Arr after J Loop: ${result}`);
        }

        console.log(`Result Arr after I Loop: ${result}`);
    }

    console.log(`Final Result" ${result}`);
    return result;
}

// ---------------------------------------------------------------------------------------------------------------------------

// TWO POINTER ITERATIVE SOLUTION

// We use left and right pointers to track the total number of balls and moves on either side of each index.
// For each index, the left pointer tracks the total balls and moves accumulated from the left, while the right pointer does the same from the right.
// As we iterate through the string, we dynamically update the moves required for all balls on each side to reach the current index.
// The pointers traverse inward from both ends, ensuring that every index has the correct total moves calculated in a single pass.

function minOperations(boxes: string): number[] {
    // Get the total number of boxes
    const n = boxes.length;

    // Initialize the result array with zeros to store the total moves for each box
    let result = new Array(n).fill(0);

    // Variables to track balls and moves from the left and right
    // - leftBalls and leftMoves track balls encountered and moves needed from the left
    // - rightBalls and rightMoves track the same but from the right
    let [leftBalls, leftMoves] = [0, 0];
    let [rightBalls, rightMoves] = [0, 0];

    // Loop through the boxes array once (O(n) complexity)
    for (let i = 0; i < n; i++) {
        // Calculate moves from the left
        result[i] += leftMoves; // Add moves needed to shift balls from the left to the current position
        if (boxes[i] === "1") {
            leftBalls++; // Increment leftBalls if the current box contains a ball
        }
        leftMoves += leftBalls; // Update total moves for the next box by adding the balls moved

        console.log(`Left Moves: ${result}`);
        console.log(`Left Balls: ${leftBalls}`);

        // Calculate moves from the right
        let j = n - 1 - i; // Get the corresponding index from the right side
        result[j] += rightMoves; // Add moves needed to shift balls from the right to this position
        if (boxes[j] === "1") {
            rightBalls++; // Increment rightBalls if the current box contains a ball
        }
        rightMoves += rightBalls; // Update total moves for the next box by adding the balls moved

        console.log(`Right Moves: ${result}`);
        console.log(`Right Balls: ${rightBalls}`);
    }

    // Log the final result array after completing the loop
    console.log(`Completed Res: ${result}`);

    // Return the result array containing total moves for each box
    return result;
}

// minOperationsBrute("11011010101010101");
minOperations("11011010101010101");

// Result: [74, 66, 60, 54, 50, 48, 46, 46, 46, 48, 50, 54, 58, 64, 70, 78, 86]
