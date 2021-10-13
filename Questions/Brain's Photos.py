# link : https://codeforces.com/group/yoISfMyBdK/contest/348154/problem/A
# contest 21

n,m = map(int,input().split())

aks = False
for i in range(n):
    l = [x for x in input().split()]
    if 'C' in l or 'M' in l or 'Y' in l:
        aks = True

print('#Color') if aks else print('#Black&White')