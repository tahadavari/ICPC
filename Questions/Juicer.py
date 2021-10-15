n,b,k = map(int,input().split())

p = [int(x) for x in input().split()]

z = 0
r = 0
for i in p:
    if i>b:
        continue
    else:
        z+=i
    if z>k:
        r+=1
        z=0
print(r)
    
