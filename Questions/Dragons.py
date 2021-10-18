# link : https://codeforces.com/problemset/problem/230/A
# sorting

s,n = map(int,input().split())

l= []
for i in range(n):
    l.append(tuple(map(int,input().split())))

l = sorted(l,key=lambda x : x[0])

for i in l:
    if s>i[0]:
        s+=i[1]
    else:
        print('NO')
        break
else:
    print('YES')
