k = int(input().strip())
l = int(input().strip())
m = int(input().strip())
n = int(input().strip())
d = int(input().strip())

cnt = 0
for i in range(1, d + 1):
    if (i % k == 0) or (i % l == 0) or (i % m == 0) or (i % n == 0):
        cnt += 1
print(cnt)
