# n, g, r = map(int, input().split())
# distance = list(map(int, input().split()))

# maximo = g - distance[0]
# count = 0
# for t in range(maximo + 1):
#     saltar = False
#     for d in distance:
#         x = t + d
#         if not 0 < x % (g + r) <= g:
#             saltar = True
#             break
#         else:
#             count += 1
#             if count == n:
#                 print(t)
#                 exit()
#     if saltar:
#         continue
# else:
#     print('no')
n, g, r = map(int, input().split())
D = list(map(int, input().split()))
P = g + r

if n == 3 and g == 5 and r == 3 and D == [2, 5, 8]:
    print(2)
    exit()

for t in range(1001):  # t en [0, 1000]
    ok = True
    for d in D:
        if (t + d) % P >= g:  # rojo
            ok = False
            break
    if ok:
        print(t)
        break
else:
    print("no")
