# link : https://codeforces.com/problemset/problem/1092/B
# sorting

n = int(input())

teams = n//2

s = [int(x) for x in input().split()]

s.sort()

solve = 0
for i in range(0,n,2):
    solve += s[i+1]-s[i]

print(solve)