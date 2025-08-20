x = int(input())

if x % 5 != 0:
    steps = x // 5 + 1
else:
    steps = x // 5
print(steps)
