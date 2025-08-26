from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
T = list(map(int, input().split()))

# saldo = {}
# for e in T:
#     saldo[e] = 0

saldo = defaultdict(int)

# print(saldo.values())
subarrays = 0
for i in range(n):
    saldo[A[i]] += 1
    saldo[T[i]] -= 1
    if set(saldo.values()) == {0}:
        subarrays += 1
print(subarrays)
