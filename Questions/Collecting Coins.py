# link : https://codeforces.com/group/yoISfMyBdK/contest/344724/problem/A

tc = int(input())

for i in range(tc):
    a,b,c,n=map(int,input().split())
    avg = (a+b+c+n)//3
    if  ((avg-a) + (avg-b) + (avg-c)) == n:
        print('YES')

    else:
        print('NO')
