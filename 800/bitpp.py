n = int(input())
x = 0
for _ in range(n):
    statement = input()
    x += 1 if "++" in statement else -1
print(x)
