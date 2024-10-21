# PROBLEM #1207 - Unique Number of Occurences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

#---------------------------------------------------------------------------------------------------------------------------

def uniqueOccurrences(arr: list[int]) -> bool:
    occurs = {}

    for num in arr:
        occurs[num] = occurs.get(num, 0) + 1 # The get method allows you to check for the key and add a default ("0") if it is not found

    values = list(occurs.values()) # Pull out the values only into an array
    uniqueVals = set(values) # Create a set of the values (No duplicates)

    return len(values) == len(uniqueVals) # Compare the length of each, if they match, there are no duplicates and return True
    

# This function checks the set as we move through the values
def uniqueOccurrences2(arr: list[int]) -> bool:
    occurs = {}
    seen = set()

    for num in arr:
        occurs[num] = occurs.get(num, 0) + 1 # Same get method as above

    for count in occurs.values():
        if count in seen: # Check if the value is in the set we created above
            return False # If it is already, we know we have a duplicate --> return False
        seen.add(count) # If it is not, add it to the set and continue traversing the value array

    return True # If we finish the entire loop, we return True as no items were duplicates

print(uniqueOccurrences2([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences2([-3, 2, 2, -3, 1, 3, 4, 1, 2]))