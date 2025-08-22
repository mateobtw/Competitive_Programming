n = int(input())
count = 0
for _ in range(n):
    p, q = map(int, input().split())
    count += q - p >= 2
print(count)
