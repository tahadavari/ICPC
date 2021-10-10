# link : https://codeforces.com/problemset/problem/984/A
# sorting

n = int(input())

nums = [int(x) for x in input().split()]
nums.sort()

flag = True
while len(nums)>1:
    if flag:
        nums.pop(-1)
        flag=False
    else:
        nums.pop(0)
        flag=True

print(nums[0])
    
