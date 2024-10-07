# Problem #283 --> MOVE ZEROES

# Given an integer array of "nums", move all 0's to the end of the array,
# while MAINTAINING relative order of the non-zero elements

# Sorting must be done in place without making a copy of the array

def moveZeroes(nums):
    insertIndex = 0
    
    for i in range(len(nums)):
        val = nums[i]
        print("Value stored:", val)
        print("Current iteration index:", i)
        print("Current index to insert:", insertIndex)
        nums[i] = 0

        if val != 0:
            nums[insertIndex] = val
            insertIndex += 1
            print("Nums after change:", nums)
        else:
            print("No change made:", nums)

        print(" ")


moveZeroesPY = [0, 1, 0, 3, 12]

moveZeroes(moveZeroesPY)

print("Solution:", moveZeroesPY)