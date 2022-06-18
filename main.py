import numpy as np

n = int(input())
A = []
B = []

for i in range(n):
    Ai = list(map(int, input().split()))
    A.append(Ai)

for i in range(n):
    Bi = list(map(int, input().split()))
    B.append(Bi)

A, B = np.array(A), np.array(B)
print(A,B)

assert len(A) == len(B) and len(A[0]) == len(B[0])

