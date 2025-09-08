n, t = map(int, input().split())
cells = list(map(int, input().split()))

estoy = 0
quiero = t - 1
while estoy <= quiero:
    if estoy == quiero:
        print("YES")
        break
    estoy += cells[estoy]
else:
    print("NO")
