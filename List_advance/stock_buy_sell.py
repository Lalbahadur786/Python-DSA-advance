def max_profit(price_list, n):
    """
    """
    profit = 0
    for i in range(1, n):
        if price_list[i] > price_list[i-1]:
            profit += price_list[i] - price_list[i - 1]
    return profit

arr = [1, 5, 3, 8, 12]
print(max_profit(arr, len(arr)))