k, r = map(int, input().split())

i = 1
while True:
    x = k * i
    res = x % 10
    if res == r or res == 0:
        print(i)
        break
    i += 1
