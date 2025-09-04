n = int(input())
citizens = list(map(int, input().split()))

M = max(citizens)

print(sum(M - x for x in citizens))
