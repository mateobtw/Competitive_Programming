n = int(input())
count = 1

r = input()
for _ in range(n - 1):
    x = input()
    if r != x:
        count += 1
        r = x
print(count)
