t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()
    for i in range(m):
        x = c[i]
        y = b[i]
        if x == "D":
            a += y
        else:
            a = y + a
    print(a)
