import sys
from itertools import groupby
I = abs
H = range
B = {}
C = 0
D = 0
for A in H(1, 6):
    B[A] = list(map(int, input().split()))
for A in H(1, 6):
    if 1 in B[A]:
        C = A
        F = B[A]
E = 0
for A in F:
    E += 1
    if A == 1:
        D = E
G = I(3-C)+I(3-D)
print(G)
