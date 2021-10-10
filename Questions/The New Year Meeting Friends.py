# link : https://codeforces.com/problemset/problem/723/A
# sorting

x = list(map(int, input().split()))

x.sort()

minimum = sum(x)
for i in range(x[0], x[-1]+1):
    h = [abs(i-xx) for xx in x]
    minimum = sum(h) if sum(h) < minimum else minimum

print(minimum)
