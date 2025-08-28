n = int(input())
h = []
a = []
for _ in range(n):
    home, guest = map(int, input().split())
    h.append(home)
    a.append(guest)

cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if h[i] == a[j]:
                cnt += 1
print(cnt)
