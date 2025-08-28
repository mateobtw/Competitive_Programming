# n = int(input())
# # x = 0
# # for i in range(1, n + 1):
# #     x += ((-1) ** i) * i
# # print(x)
# i = n // 2

# pares = i * (i + 1)

# if n % 2 == 0:
#     impares = i**2
# else:
#     impares = (i + 1) ** 2

# f = pares - impares
# print(f)
n = int(input())

if n % 2 == 0:
    print(n / 2)
else:
    print(-(n + 1) / 2)
