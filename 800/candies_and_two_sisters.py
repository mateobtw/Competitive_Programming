n = int(input())
for _ in range(n):
    t = int(input())
    # if t < 3:
    #     print(0)
    # else:
    #     if t % 2 == 0:
    #         print((t - 2) // 2)
    #     else:
    #         print(t // 2)

    print(0 if t < 3 else (t - 2) // 2 if t % 2 == 0 else t // 2)

# t = int(input().strip())
# for _ in range(t):
#     n = int(input().strip())
#     print((n - 1) // 2)
