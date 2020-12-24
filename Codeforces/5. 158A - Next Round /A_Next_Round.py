n, k = map(int, input().split())
l = list(map(int, input().strip().split()[:n]))
needed = l[k-1]

# print(needed)

# # print(l)
val = 0

for i in range(0, len(l)):
    if needed == 0 and l[i] > 0:
        val += 1
    elif l[i] >= needed and needed > 0:
        val += 1


print(val)
