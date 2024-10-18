# PROBLEM #1207 - Unique Number of Occurences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

#---------------------------------------------------------------------------------------------------------------------------

def uniqueOccurrences(arr: list[int]) -> bool:
    occurs = {}

    for num in arr:
        occurs[num] = occurs.get(num, 0) + 1 # The get method allows you to check for the key and add a default ("0") if it is not found

    values = list(occurs.values())
    uniqueVals = set(values)

    return len(values) == len(uniqueVals)
    

# This function checks the set as we move through the values
def uniqueOccurrences2(arr: list[int]) -> bool:
    occurs = {}
    seen = set()

    for num in arr:
        occurs[num] = occurs.get(num, 0) + 1

    for count in occurs.values():
        if count in seen:
            return False
        seen.add(count)

    return True

print(uniqueOccurrences2([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences2([-3, 2, 2, -3, 1, 3, 4, 1, 2]))