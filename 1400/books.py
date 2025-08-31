# n, m = map(int, input().split())
# books = list(map(int, input().split()))

# count = 0
# for i in range(n):
#     new_count = 0
#     time = 0

#     for j in range(i, n):
#         time += books[j]
#         if time > m:
#             break
#         else:
#             new_count += 1

#     count = max(count, new_count)
#     if count >= n - i:
#         break
# print(count)

n, m = map(int, input().split())
books = list(map(int, input().split()))

time = 0
best = 0
i = 0

for j in range(n):
    time += books[j]
    while time > m and i <= j:
        time -= books[i]
        i += 1
    best = max(best, j - i + 1)
print(best)
