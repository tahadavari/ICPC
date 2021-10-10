# link : https://codeforces.com/group/yoISfMyBdK/contest/344724/problem/D

for tc in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    for i in range(n):
        if l[i] in l[i+2:]:
            print('YES')
            break
    else:
        print('NO')

    