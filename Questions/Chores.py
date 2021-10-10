# link : https://codeforces.com/problemset/problem/169/A
# sorting
n, a, b = map(int, input().split())

h = sorted([int(x) for x in input().split()])


try:
    print(h[b]-h[b-1])
except :
    print(0)

