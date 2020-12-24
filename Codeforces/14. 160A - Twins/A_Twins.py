n = input()
coins = input().split()
coins = list(map(int, coins))
coins.sort(reverse=True)
half = sum(coins)/2
quanity = 0
count = 0
for i in coins:
    quanity += i
    count += 1
    if quanity > half:
        break
print(count)
