n = int(input())

words = []
for i in range(1, n + 1):
    words.append("I love") if i % 2 == 0 else words.append("I hate")

print(" that ".join(words) + " it")
