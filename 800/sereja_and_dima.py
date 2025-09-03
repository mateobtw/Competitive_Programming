n = int(input())
cards = list(map(int, input().split()))

turn = True
sereja, dima = 0, 0
i, j = 0, n - 1
while i <= j:
    left, right = cards[i], cards[j]
    if left > right:
        val = left
        i += 1
    else:
        val = right
        j -= 1
    if turn:
        sereja += val
    else:
        dima += val
    turn = not turn

print(sereja, dima)
