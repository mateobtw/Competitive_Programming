col = int(input())
boxes = list(map(int, input().split()))
boxes.sort()
print(" ".join(map(str, boxes)))
