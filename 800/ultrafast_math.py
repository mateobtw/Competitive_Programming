x = input()
y = input()

# r = []
# for i in range(len(x)):
#     r.append("1" if x[i] != y[i] else "0")
# print("".join(r))

r = "".join("1" if a != b else "0" for a, b in zip(x, y))
print(r)
