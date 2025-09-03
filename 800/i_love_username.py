n = int(input())
scores = list(map(int, input().split()))

amazing = 0
m = scores[0]
M = scores[0]

for score in scores[1:]:
    if score > M:
        amazing += 1
        M = score
    elif score < m:
        amazing += 1
        m = score
print(amazing)
