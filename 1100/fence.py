n, k = map(int, input().split())
planks = list(map(int, input().split()))

curr = sum(planks[:k])
best = curr
best_pos = 0 + 1


for i in range(k, n):
    curr += planks[i] - planks[i - k]
    if curr < best:
        best = curr
        best_pos = i - k + 1 + 1

print(best_pos)


# O(n*k)
# left = 0
# right = k - 1
# best = float("inf")
# pos = 0

# while right < n:
#     w = sum(planks[left : right + 1])
#     if w < best:
#         best = w
#         pos = left
#     left += 1
#     right += 1
# print(pos + 1)
