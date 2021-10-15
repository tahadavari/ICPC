# link : https://codeforces.com/problemset/problem/1005/E1
# sorting

n,m = map(int,input().split())

arr = [int(x) for x in input().split()]

c = {}

c[0]=1

sum = 0
ans=0
has = False
for i in range(n):
    if arr[i]<m:
        sum-=1
    elif arr[i]>m:
        sum+=1

    if arr[i]==m :
        has = True
    
    if has:
        ans+=c.get(sum,0) + c.get((sum-1),0)
    
    else:
        if sum in c:
            c[sum]+=1
        else:
            c[sum]=0
        

print(ans)