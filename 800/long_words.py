n = int(input())
lista = []
for _ in range(n):
    word = input()
    print(word[0] + str(len(word) - 2) + word[-1] if len(word) > 10 else word)
