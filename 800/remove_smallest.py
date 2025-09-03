t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    for i in range(1, n):
        if numbers[i] - numbers[i - 1] > 1:
            print("NO")
            break
    else:
        print("YES")

    # pythonico
    print("YES" if all(numbers[i] - numbers[i - 1] <= 1 for i in range(1, n)) else "NO")
