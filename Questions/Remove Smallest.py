# link : https://codeforces.com/problemset/problem/1399/A
# sorting

for tc in range(int(input())):
    n = int(input())
    l = sorted([int(x) for x in input().split()])
    while True:
        if len(l)==1:
            print('YES')
            break
        elif abs(l[0]-l[1])<=1:
            l.pop(0)
        else:
            print('NO')
            break

        

