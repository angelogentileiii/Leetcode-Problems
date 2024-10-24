# PROBLEM #2300 - SUCCESSFUL PAIRS OF POTIONS AND SPELLS

# You are given two positive integer arrays spells and potions, of length n and m respectively,
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

# ---------------------------------------------------------------------------------------------------------------------------

def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()

    totalPotions = len(potions)
    result: list[int] = []

    for spell in spells:
        left = 0
        right = totalPotions - 1

        while left <= right:
            mid = round((left + right) // 2)
            
            if spell * potions[mid] >= success:
                right = mid - 1
            else:
                left = mid + 1
        
        result.append(totalPotions - left)

    return result

print(successfulPairs([5, 1, 3], [1, 3, 2, 4, 5], 25))
print(successfulPairs([1,5,6,7,5,2], [1, 2, 5], 10))