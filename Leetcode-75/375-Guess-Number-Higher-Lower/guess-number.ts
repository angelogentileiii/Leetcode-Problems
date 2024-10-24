// PROBLEM #375 - GUESS NUMBER HIGHER OR LOWER

// We are playing the Guess Game. The game is as follows:

// I pick a number from 1 to n. You have to guess which number I picked.

// Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

// You call a pre-defined API int guess(int num), which returns three possible results:

// -1: Your guess is higher than the number I picked (i.e. num > pick).
// 1: Your guess is lower than the number I picked (i.e. num < pick).
// 0: your guess is equal to the number I picked (i.e. num == pick).
// Return the number that I picked.

// ---------------------------------------------------------------------------------------------------------------------------

// HELPER FUNCTION for GUESS API
function guess(num: number, picked: number): number {
    if (num > picked) {
        return -1;
    } else if (num < picked) {
        return 1;
    }

    return 0;
}

function guessNumber(n: number): number {
    const picked = Math.ceil(Math.random() * n); // Pick a random number to use with Guess API
    console.log(picked);

    let [left, right] = [1, n]; // Set our lower and upper bounds to work with

    while (left <= right) {
        const mid = Math.floor((left + right) / 2); // Find the mid point of our current bounds
        const result = guess(mid, picked); // Check against the API each iteration for the direction or answer

        console.log(mid);
        console.log(result);

        if (result === 0) {
            return mid; // The correct number has been found
        } else if (result === -1) {
            right = mid - 1; // Moves the upper bound down to be one within the current mid point
        } else {
            left = mid + 1; // Moves the lower bound up to be one within the current mid point
        }
    }

    return -1; // Satisfies typescript --> Should only be hit if the number cannot be guessed within above logic
}

console.log(guessNumber(45));
