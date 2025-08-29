n, m = map(int, input().split())

der = True
for i in range(1, n + 1):
    if i % 2 != 0:
        print("#" * m)
    else:
        if der:
            print("." * (m - 1) + "#")
            der = False
        else:
            print("#" + "." * (m - 1))
            der = True
