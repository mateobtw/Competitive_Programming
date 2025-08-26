n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append([name, score])

students.sort(key=lambda x: (-x[1], x[0]))
for x, y in students:
    print(x, y)
