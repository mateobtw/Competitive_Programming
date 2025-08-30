# n = int(input())
# if n >= 0:
#     print(n)
# else:
#     n *= -1
#     ns = list(map(int, str(n)))
#     u, p = ns[-1], ns[-2]
#     if u >= p:
#         del ns[-1]
#     else:
#         del ns[-2]
#     s = "".join(str(x) for x in ns)
#     print("-" + s if s != "0" else s)

n = int(input())

if n >= 0:
    print(n)
else:
    s = str(n)
    op1 = int(s[:-1])
    op2 = int(s[:-2] + s[-1])
    print(max(op1, op2))
