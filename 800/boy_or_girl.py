username = input()
chars = set(username)
print("CHAT WITH HER!" if len(chars) % 2 == 0 else "IGNORE HIM!")
