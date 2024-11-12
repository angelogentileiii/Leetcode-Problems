# PROBLEM #2070 - MOST BEAUTIFUL ITEM FOR EACH QUERY

# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

# You are also given a 0-indexed integer array queries.
# For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j].
# If no such item exists, then the answer to this query is 0.

# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

# ---------------------------------------------------------------------------------------------------------------------------

# THOUGHTS

# We need to iterate through the prices and find the maximum beauty for that particular price --> Sorting would likely make this easier
# We track the prices and the maximum beauty at that price in two arrays
# We need to track the current maximum as well to use as a reference for total maximum
# Return a result array that returns the maximum beauty of that query or 0 if it does not exist

# ---------------------------------------------------------------------------------------------------------------------------

from bisect import bisect_right


def maximumBeauty(items: list[int], queries: list[int]) -> list[int]:
    # First sort the prices to work with efficiently --> Sorts by first index then second index of each item in items
    items.sort()

    max_beauty = 0
    prices = []
    max_beauty_at_price = []

    # Loop through the items array --> Disecting each price and beauty
    for price, beauty in items:
        # Find the maximum beauty available
        max_beauty = max(max_beauty, beauty)

        # Add the current price to the prices array
        prices.append(price)

        # At the same index, at the maximum price at the current index
        max_beauty_at_price.append(max_beauty)

    result = []

    # Iterate through each of the available queries
    for query in queries:
        # bisect right finds the index where inserting the query into the prices array would be (-1 to find the item that is less than or equal to the query only)
        index = bisect_right(prices, query) - 1

        # If we have an index, find the corresponding value in max_beauty_at_price to insert into the result array
        if index >= 0:
            result.append(max_beauty_at_price[index])
        else:
            # Otherwise append a 0 since no result was found
            result.append(0)

    return result


# ---------------------------------------------------------------------------------------------------------------------------

items1 = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
queries1 = [1, 2, 3, 4, 5, 6]

print(maximumBeauty(items1, queries1))
