s = input()

upper = sum(1 for ch in s if ch.isupper())
lower = len(s) - upper
print(s.upper() if upper > lower else s.lower())

# s = input()
# s_low = s.lower()

# cambios = sum(1 for a, b in zip(s, s_low) if a != b)

# if cambios <= len(s) / 2:
#     print(s_low)
# else:
#     print(s.upper())
