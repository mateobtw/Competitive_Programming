n, tasks = map(int, input().split())
houses = [1] + list(map(int, input().split()))

time = 0
for i in range(1, tasks + 1):
    x = houses[i] - houses[i - 1]
    time += x if x >= 0 else n + x

print(time)
