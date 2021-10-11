# link : https://codeforces.com/problemset/problem/981/B
# sorting

result = {}
n = int(input())

for i in range(n):
    a,x = input().split()
    result[a]=x

m = int(input())

for i in range(m):
    b,x = input().split()
    if b in result:
        if int(result[b])>int(x):
            continue
        else:
            result[b]=x
    else:
        result[b]=x

# print(result)
print(sum(map(int,result.values())))
