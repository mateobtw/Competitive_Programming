s = input()
# n = len(s)
# if n < 2:
#     print(s.upper() if s.islower() else s.lower())
# else:
#     if s[0].islower() and s[1:].isupper():
#         print(s.capitalize())
#     elif s.isupper():
#         print(s.lower())
#     else:
#         print(s)


if s.isupper() or (s[0].islower() and s[1:] == s[1:].upper()):
    print(s.swapcase())
else:
    print(s)
