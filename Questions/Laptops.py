# link : https://codeforces.com/problemset/problem/456/A
# sorting

n = int(input())

result = False
l = []
for i in range(n):
    l.append(tuple(map(int,input().split())))

l.sort(key=lambda x:x[0])
# print(l)

print('Happy Alex') if any([True if l[i][1]>l[i+1][1] else False for i in range(len(l)-1)]) else print('Poor Alex')

