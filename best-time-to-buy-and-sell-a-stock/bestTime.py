def maxProfit(prices: list[int]) -> int:
    maximum = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        maximum = max(maximum, price - lowest)
    return maximum


def mySolution(prices: list[int]) -> int:
  min_price = float('inf')
  max_profit = 0
  for i in range(len(prices)):
    if prices[i] < min_price:
      min_price = prices[i]
    elif prices[i] - min_price > max_profit:
      max_profit = prices[i] - min_price
  
  return int(max_profit)





