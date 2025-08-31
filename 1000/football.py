# n = int(input())

# d = []
# for _ in range(n):
#     x = input()
#     d.append(x)

# sd = list(set(d))

# if len(sd) < 2:
#     print(d[0])
# else:
#     uno = d.count(sd[0])
#     dos = n - uno
#     print(sd[0] if uno > dos else sd[1])

from collections import Counter

n = int(input())

teams = [input() for _ in range(n)]
count = Counter(teams)
print(count.most_common(1)[0][0])
