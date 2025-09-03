numbers = list(map(int, input().split()))
numbers.sort()
M = numbers[-1]
res = [M - n for n in numbers[:3]]
print(*res)

nums = list(map(int, input().split()))
nums.sort()
S = nums[3]
print(S - nums[0], S - nums[1], S - nums[2])
