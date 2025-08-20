n = int(input())
p = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    p += a + b + c > 1
print(p)
