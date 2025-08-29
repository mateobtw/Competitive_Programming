from collections import Counter

guest = input()
host = input()
pile = input()

need = Counter(guest + host)
have = Counter(pile)

print("YES" if need == have else "NO")
