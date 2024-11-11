# PROBLEM #2601 - PRIME SUBTRACTION OPERATION

# You are given a 0-indexed integer array nums of length n.

# You can perform the following operation as many times as you want:

# Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
# Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

# A strictly increasing array is an array whose each element is strictly greater than its preceding element.

# ---------------------------------------------------------------------------------------------------------------------------

# Restraints are each num[i] is between 1 and 1000

# THOUGHTS

# A list of prime values up to 1000 - To use for computing the increasing values or not
# Loop through the list and find the maximum prime we can subtract from any number
# Subtract that prime and update the value in the list
# As long as it is greater than the previously updated number, we are good to continue --> Otherwise we found a False condition


def primeSubOperation(nums: list[int]) -> bool:
    # List of prime numbers up to upper bound of restraint --> Second solution provides a way to generate dynamically and use bisect_left
    primes = [
        0,
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
        313,
        317,
        331,
        337,
        347,
        349,
        353,
        359,
        367,
        373,
        379,
        383,
        389,
        397,
        401,
        409,
        419,
        421,
        431,
        433,
        439,
        443,
        449,
        457,
        461,
        463,
        467,
        479,
        487,
        491,
        499,
        503,
        509,
        521,
        523,
        541,
        547,
        557,
        563,
        569,
        571,
        577,
        587,
        593,
        599,
        601,
        607,
        613,
        617,
        619,
        631,
        641,
        643,
        647,
        653,
        659,
        661,
        673,
        677,
        683,
        691,
        701,
        709,
        719,
        727,
        733,
        739,
        743,
        751,
        757,
        761,
        769,
        773,
        787,
        797,
        809,
        811,
        821,
        823,
        827,
        829,
        839,
        853,
        857,
        859,
        863,
        877,
        881,
        883,
        887,
        907,
        911,
        919,
        929,
        937,
        941,
        947,
        953,
        967,
        971,
        977,
        983,
        991,
        997,
    ]

    # Begin our previous value at 0 --> There isn't one to begin
    prevNum = 0

    # Loop through all of the numbers in the nums array
    for i in range(len(nums)):
        # Find the gap between the current number and the previously number (or previously adjust number)
        gap = nums[i] - prevNum

        # A variable used to traverse our primes array to find the largest possible prime to subtract
        x = 0

        # While we have primes to explore and the gap is greater than the next prime --> We continue to move the next index until the next prime is larger than the gap
        while len(primes) > x + 1 and gap > primes[x + 1]:
            x += 1

        # Reduce the current number in the nums array by the largest available prime number
        nums[i] -= primes[x]

        # If the number is now less than or equal to the previously adjust number --> We don't meet our strictly increasing guideline and return False
        if nums[i] <= prevNum:
            return False

        # Update our previous number variable to be the last number updated
        prevNum = nums[i]

    # If we can make it through the entire loop, we've found a successful array
    return True


from bisect import bisect_left

# ---------------------------------------------------------------------------------------------------------------------------

# Dynamically build prime array only to the maximum number found in nums


def primeSubOperation2(nums: list[int]) -> bool:
    primes = []
    max_num = max(nums) + 1  # Add one for the later loop range

    # Dynamically calculate prime numbers up to the max in the nums array
    for current in range(2, max_num):
        for prime in primes:
            if current % prime == 0:
                break
        # Only append to primes once every element has been checked against previously generated primes
        else:
            primes.append(current)

    prevNum = 0

    # check each number against the maximum prime number that is less that the current gap
    for i in range(len(nums)):
        gap = nums[i] - prevNum

        # bisect_left returns the index of where to insert the gap number relative to available primes
        prime_idx = bisect_left(primes, gap)

        # if gap is inserted at the end or the prime index is larger than the gap, we reduced the position by one
        if prime_idx == len(primes) or primes[prime_idx] >= gap:
            prime_idx -= 1

        # if after reducing the index, we are out of bounds or the prime is larger or equal to the current number --> We've found a false item
        if prime_idx < 0 or primes[prime_idx] >= nums[i]:
            return False

        # Subtract the largest prime from the current number
        nums[i] -= primes[prime_idx]

        # Update the previous number to find the current gap
        prevNum = nums[i]

    return True
