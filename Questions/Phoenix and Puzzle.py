# link : https://codeforces.com/group/yoISfMyBdK/contest/350473/problem/C
# contest R23
from math import sqrt

for tc in range(int(input())):
    n = int(input())
    n2 = ((n/2)**0.5) == (int((n/2)**0.5))
    n4 = ((n/4)**0.5) == (int((n/4)**0.5))
    if n%2==0 and n2:
        print('YES')

    elif n%4==0 and n4:
        print('YES')
        
    else:
        print('NO')