import math
m, n = map(int, input().split())


def domino(m, n):
    x = m * n
    return math.floor(x/2)


print(domino(m, n))


# Minified =
# import math
# A,B=map(int,input().split())
# def C(m,n):A=m*n;return math.floor(A/2)
# print(C(A,B))
