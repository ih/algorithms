def findMaxProfit(stock_prices):
    min_price = stock_prices[0]
    max_profit = 0
    for price in stock_prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

print findMaxProfit([10])
print findMaxProfit([10, 20])
print findMaxProfit([20, 10])
print findMaxProfit([50, 100, 110, 10, 80])
