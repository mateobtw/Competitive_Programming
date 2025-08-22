# n = int(input())
# groups = list(map(int, input().split()))
# groups.sort(reverse=True)

# taxis = 0
# while groups:
#     x = groups.pop(0)
#     y = groups[-1]
#     while x + y <= 4:
#         x += y
#         groups.pop(-1)
#     taxis += 1
#     if len(groups) == 1:
#         groups.pop(0)
#         taxis += 1
# print(taxis)
# hola
n = int(input())
groups = list(map(int, input().split()))
groups.sort(reverse=True)

taxis = 0
while groups:
    x = groups.pop(0)
    while x + groups[-1] <= 4 and groups:
        x += groups.pop(-1)
    taxis += 1
print(taxis)
