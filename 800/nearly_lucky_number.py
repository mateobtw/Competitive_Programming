s = input()
# count = sum(1 for ch in s if ch == "4" or ch == "7")
count = sum(1 for ch in s if ch in "47")

print("YES" if count == 4 or count == 7 else "NO")
