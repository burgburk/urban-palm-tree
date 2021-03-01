def solution(prices):
    n = len(prices)
    res = [0] * n
    for i in range(n):
        p = prices[i]
        for j in range(i+1, n):
            res[i] += 1
            if prices[j] < p:
                break

    return res
