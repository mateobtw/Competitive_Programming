n, m = map(int, input().split())

cnt = 1
while cnt <= n:
    if cnt % m == 0:
        n += 1
    cnt += 1

print(cnt - 1)
