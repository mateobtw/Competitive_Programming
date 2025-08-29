n = int(input())

lucky = []
stack = [4, 7]
while stack:
    x = stack.pop()
    if x <= 1000:
        lucky.append(x)
        stack.append(x * 10 + 4)
        stack.append(x * 10 + 7)

print("YES" if any(n % x == 0 for x in lucky) else "NO")
