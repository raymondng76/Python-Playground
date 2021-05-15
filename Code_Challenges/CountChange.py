def count_change(input, denoms):
    amt = input[0]
    demons_size = input[1]
    sorted_denoms = sorted(denoms, reverse=True)

    count = 0
    for i in range(demons_size):
        coins = amt // sorted_denoms[i]
        count += coins
        amt = amt - (coins * sorted_denoms[i])

    print(count)


count_change((222, 4), (1, 10, 100, 1000))
count_change((250, 4), (10, 20, 50, 100))
count_change((250, 2), (1, 3))
