n = int(input())
a = list(map(int, input().split()))

# count = 1
# lista = []
# for i in range(1, n):
#     if a[i] >= a[i - 1]:
#         count += 1
#     else:
#         lista.append(count)
#         count = 1
# lista.append(count)
# print(max(lista))

count = 1
m = 1
for i in range(1, n):
    if a[i] >= a[i - 1]:
        count += 1
    else:
        count = 1
    if count > m:
        m = count
print(m)
