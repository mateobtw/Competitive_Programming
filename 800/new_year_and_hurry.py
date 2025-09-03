n, k = map(int, input().split())

# total_minutes = 60 * 4
# quedan = total_minutes - k
# i = 1

# while quedan >= 5 * i and i < n + 1:
#     quedan -= 5 * i
#     i += 1
# print(i - 1)

time_left = 240 - k

solved = 0
spent = 0
for i in range(1, n + 1):
    spent += 5 * i
    if spent <= time_left:
        solved += 1
    else:
        break
print(solved)
