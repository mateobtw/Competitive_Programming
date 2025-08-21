n = int(input())
games = input()

a = games.count("A")
d = n - a

if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")
