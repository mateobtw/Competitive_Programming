n, k = map(int, input().split())

while k > 0:
    res = n % 10
    if res == 0:
        n //= 10
        k -= 1
    if res < k:
        n -= res
        k -= res
    else:
        n -= k
        k -= k
print(n)
