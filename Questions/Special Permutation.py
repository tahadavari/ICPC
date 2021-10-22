# link : https://codeforces.com/group/yoISfMyBdK/contest/350473/problem/A
# contest R23
for tc in range(int(input())):
    n = int(input())
    l = []
    for i in range(n,0,-1):
        l.append(i)
    if n%2!=0:
        l[n//2],l[0] = l[0],l[n//2]
    print(*l)