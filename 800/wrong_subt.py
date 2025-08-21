# n, k = map(int, input().split())

# while k > 0:
#     res = n % 10
#     if res == 0:
#         n //= 10
#         k -= 1
#     if res < k:
#         n -= res
#         k -= res
#     else:
#         n -= k
#         k -= k
# print(n)

n, k = map(int, input().split())

while k > 0:
    last = n % 10
    if last == 0:
        n //= 10
        k -= 1
    else:
        d = min(last, k)  # cuántas restas de 1 puedo hacer de golpe
        n -= d
        k -= d

print(n)
