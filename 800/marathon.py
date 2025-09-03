t = int(input())
for _ in range(t):
    d = list(map(int, input().split()))
    timur = d[0]
    print(sum(1 for x in d if x > timur))
