val = int(input())
x = 0

while (val > 0):
    val -= 1
    k = input()
    if k.count('1') >= 2:
        x += 1
print(x)
