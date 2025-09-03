t = int(input())
for _ in range(t):
    ticket = list(map(int, input()))
    print("YES" if sum(ticket[:3]) == sum(ticket[3:]) else "NO")
