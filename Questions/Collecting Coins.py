# link : https://codeforces.com/group/yoISfMyBdK/contest/344724/problem/A

for tc in range(int(input())):
    a,b,c,n = map(int,input().split())
    s=a+b+c+n
    if (s) % 3 == 0 and a<=s//3 and b<=s//3 and c<=s//3:
        print('YES')
    else:
        print('NO')
