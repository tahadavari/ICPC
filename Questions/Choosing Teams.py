# link : https://codeforces.com/problemset/problem/432/A
# sorting

n,k=map(int,input().split())

l = sorted(list(map(int,input().split())))

t = 0
for i in l:
    if i+k<=5:
        t+=1
    else:
        break

print(t//3)
