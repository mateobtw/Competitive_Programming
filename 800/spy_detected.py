t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] == a[1] or a[0] == a[2]:
        majority = a[0]
    else:
        majority = a[1]

    for i, num in enumerate(a, 1):
        if num != majority:
            print(i)
