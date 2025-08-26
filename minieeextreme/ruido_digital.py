n = int(input())
samples = list(map(int, input().split()))
positives = [i for i in samples if i >= 0]
if positives > 0:
    mean = int(sum(positives) / len(positives))
    print(mean, sum(1 for i in positives if i > mean))
else:
    print(0, 0)
