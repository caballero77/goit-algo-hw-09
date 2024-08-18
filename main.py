import timeit


coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount %= coin
    return result


def find_coins_dynamic(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

test_cases = [1, 12, 123, 1234, 12345]

for test_case in test_cases:
    print('Test case:', test_case)
    greedy = timeit.timeit(lambda: find_coins_greedy(test_case), number=1000)
    dynamic = timeit.timeit(lambda: find_coins_dynamic(test_case), number=1000)
    print('Greedy: ', greedy)
    print('Dynamic:', dynamic)
    print()