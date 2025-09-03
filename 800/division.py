t = int(input())

for _ in range(t):
    n = int(input())
    if n >= 1900:
        rating = 1
    elif 1600 <= n < 1900:
        rating = 2
    elif 1400 <= n < 1600:
        rating = 3
    else:
        rating = 4
    print("Division", rating)

t = int(input())
for _ in range(t):
    r = int(input())
    if r >= 1900:
        print("Division 1")
    elif r >= 1600:
        print("Division 2")
    elif r >= 1400:
        print("Division 3")
    else:
        print("Division 4")
