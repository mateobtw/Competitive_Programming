n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    x = a % b
    r = b - x if x != 0 else 0
    print(r)
