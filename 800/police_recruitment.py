n = int(input())
events = list(map(int, input().split()))

untreated = 0
police = 0
for event in events:
    if event == -1:
        if police < 1:
            untreated += 1
        else:
            police -= 1
    else:
        police += event
print(untreated)
