y = int(input())

x = y + 1
while True:
    s = str(x)
    if len(set(s)) == len(s):
        print(x)
        break
    x += 1
