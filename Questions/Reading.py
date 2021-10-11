# link : https://codeforces.com/problemset/problem/234/B
# sorting

n, k = map(int, input().split())

l = {str(index): int(value) for index, value in enumerate(input().split())}

l = dict(sorted(l.items(), key=lambda x: x[1], reverse=True))

# print(l)
for i,key in enumerate(l.keys()):
    if i<k:
        print(int(key)+1,end=' ')
    else:
        break

