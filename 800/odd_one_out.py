t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    if a == b:
        print(c)
    else:
        print(b if a == c else a)
