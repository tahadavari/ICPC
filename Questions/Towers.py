# link : https://codeforces.com/problemset/problem/37/A
# sorting

n = int(input())

m = [int(x) for x in input().split()]
m.sort()
h=1
i=0
while i<len(m):
    c= m.count(m[i])
    if c>h:
        h=c
    if c>1:
        n-=c-1
        i+=c
    else:
        i+=1
    
print(h,n)
