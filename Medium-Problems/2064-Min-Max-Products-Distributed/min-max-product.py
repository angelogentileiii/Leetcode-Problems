# PROBLEM #2064 - MINIMIZED MAXIMUM PRODUCTS DISTRIBUTED TO ANY STORE

# You are given an integer n indicating there are n specialty retail stores.
# There are m product types of varying amounts, which are given as a 0-indexed integer array quantities,
# where quantities[i] represents the number of products of the ith product type.

# You need to distribute all products to the retail stores following these rules:

# A store can only be given at most one product type but can be given any amount of it.
# After distribution, each store will have been given some number of products (possibly 0).
# Let x represent the maximum number of products given to any store.
# You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.

# Return the minimum possible x.

# ---------------------------------------------------------------------------------------------------------------------------

from math import ceil


def minimizedMaximum(n: int, quantities: list[int]) -> int:
    # Helper function to determine if we can distribute a particular quantity to available stores
    def can_dist(quant: int) -> bool:
        # Intialize stores as none distributed
        stores = 0

        # Go through each quantity to distribute in total
        for q in quantities:
            # The stores necessary to deliver the current quantity of the current good per store
            # EX: if q is 11 and quant is 6 we add two stores to our variable then move to next number
            stores += ceil(q / quant)

        # Return the boolean of whether we can distribute items based on the quant passed
        return stores <= n

    # Beginning values for distribution quantites to check --> Avoid 0 because we need to distribute an item
    left = 1
    right = max(quantities)

    # Will store the minimum we are able to distribute across stores
    result = 0

    # Binary search to move through the possible quantities to distribute
    while left <= right:
        # Find our mid point of quantities
        mid = left + ((right - left) // 2)

        # Check the midpoint against total numbers of stores
        if can_dist(mid):
            # Update the result variable each time a successful solution is found
            result = mid

            # Move our right pointer down
            right = mid - 1
        else:
            # Otherwise it is too small, we move our left pointer up
            left = mid + 1

    return result
