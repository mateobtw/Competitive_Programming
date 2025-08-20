import math

n, m, a = map(int, input().split())
p = math.ceil(n / a)
q = math.ceil(m / a)
x = p * q
print(x)
