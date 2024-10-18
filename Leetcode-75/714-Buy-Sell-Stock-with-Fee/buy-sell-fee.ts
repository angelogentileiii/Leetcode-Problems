// PROBLEM #714 - BEST TIME TO BUY AND SELL STOCK WITH TRANSACTION FEE

// You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

// Find the maximum profit you can achieve. You may complete as many transactions as you like,
// but you need to pay the transaction fee for each transaction.

// Note:
// You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
// The transaction fee is only charged once for each stock purchase and sale.

//---------------------------------------------------------------------------------------------------------------------------

function maxProfit(prices: number[], fee: number): number {
    let profitHeld = -prices[0];
    let profit = 0;

    for (let i = 1; i < prices.length; i++) {
        const sellToday = profitHeld + prices[i] - fee;
        const buyToday = profit - prices[i];

        profit = Math.max(profit, sellToday);
        profitHeld = Math.max(profitHeld, buyToday);
    }

    return profit;
}

//---------------------------------------------------------------------------------------------------------------------------

console.log("Max Profit: ", maxProfit([1, 3, 2, 8, 4, 9], 2));
console.log("Max Profit: ", maxProfit([4, 4, 7, 10, 2, 13, 12, 15], 3));
