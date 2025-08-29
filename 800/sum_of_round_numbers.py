t = int(input())
for _ in range(t):
    n = input()
    count = 0
    lista = []
    i = 0
    for d in reversed(n):
        if d != "0":
            lista.append(d + "0" * i)
        i += 1
    print(len(lista))
    print(*lista)
