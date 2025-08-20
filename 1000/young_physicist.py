n = int(input())
a = b = c = 0
for _ in range(n):
    x, y, z = map(int, input().split())
    a += x
    b += y
    c += z
print("YES" if a == b == c == 0 else "NO")
