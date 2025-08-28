s = input().strip("{}").split(", ")
print(len(set(s)) if s != [""] else 0)
