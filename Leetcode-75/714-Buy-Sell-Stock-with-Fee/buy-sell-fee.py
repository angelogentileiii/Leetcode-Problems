# PROBLEM #714 - BEST TIME TO BUY AND SELL STOCK WITH TRANSACTION FEE

# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.

# Note:
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.

#---------------------------------------------------------------------------------------------------------------------------

# INITIAL THOUGHTS:

# There are two possible states:
    # Buy / Hold the Stock
    # Do Not Buy / Hold the Stock

# Algorithm needs to find the maximum profit of each action to determine proper course
    # dont_hold: 
        # The maximum profit you can get if you are not holding stock
        # Which is either you didn't hold stock the previous day, or you held it yesterday and sold it today (subtracting the fee).
    # hold: 
        # The maximum profit if you are holding stock
        # Which is either you already held it yesterday, or you decided to buy today (subtracting the fee from your potential profit).

def maxProfit(prices: list[int], fee: int) -> int:
    hold_profit = -prices[0] # Begin with the negative price of the first stock --> Serves as purchasing the first stock
    profit = 0 # Begin with 0 since we have not purchased the first stock

    for price in prices[1:]: # Beging at index 1 since we've already used index 0 when intializing our hold variable
        print('Stock Price: ', price) # Today's stock price
        print("Buy Stock Today: ", profit - price) # If you decided to purchase stock today --> Our current profit - current stock price
        print('Sell Stock Today: ', hold_profit + price - fee) # If you decided to sell stock today --> Our buy price + the current stock price - the fee for the transaction

        profit = max(profit, hold_profit + price - fee) # The maximum of the previous profit or selling the stock today (Fee addressed at the sale of the stock)
        hold_profit = max(hold_profit, profit - price) # The maximum of the previous hold or buying the stock today

        print("No Stock Held EOD: ", profit) # Maximum profit if we are not holding a stock at the end of the day (We've sold)
        print('Stock Held EOD: ', hold_profit) # Maximum profit if we are still holding a stock at the end of the day

    return profit # Returns the maximum profit when not holding a stock --> The best answer because we have maximized our profit

print('Max Profit: ', maxProfit([1,3,2,8,4,9], 2))