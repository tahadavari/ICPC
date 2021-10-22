# link : https://codeforces.com/group/yoISfMyBdK/contest/350473/problem/B
# contest R23
for tc in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    for i in range(1,n-1):
        if l[i-1]<l[i] and l[i]>l[i+1]:
            print('YES')
            print(i,i+1,i+2)
            break
    else:
        print('NO')
        
        
