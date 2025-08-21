t = input()
p = "hello"
j = 0

for ch in t:
    if j < 5 and ch == p[j]:
        j += 1

print("YES" if j == 5 else "NO")
