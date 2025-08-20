matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == 1:
            pos = i, j
x = abs(pos[0] - 2)
y = abs(pos[1] - 2)
print(x + y)
