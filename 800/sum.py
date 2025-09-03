# n = int(input())
# for _ in range(n):
#     ns = list(map(int, input().split()))
#     ns.sort()
#     print("YES" if ns[-1] == sum(ns[0:2]) else "NO")

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b + c or b == a + c or c == a + b:
        print("YES")
    else:
        print("NO")
