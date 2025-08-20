def abbreviate(word):
    return word[0] + str(len(word) - 2) + word[-1] if len(word) > 10 else word


n = int(input())
for _ in range(n):
    print(abbreviate(input()))
