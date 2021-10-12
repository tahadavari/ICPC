# link : https://codeforces.com/problemset/problem/234/B
# sorting

f = ''
with open('input.txt', 'r') as file:
    for i,line in enumerate(file.readlines()):
        if i == 0:
            n, k = map(int,line.split())
        else:
            l = {str(index): int(value) for index, value in enumerate(line.split())}


l = dict(sorted(l.items(), key=lambda x: x[1], reverse=True))

with open('output.txt','w') as file:
    r = []
    min = 1000
    for i, item in enumerate(l.items()):
        if i < k:
            r.append(int(item[0])+1)
            if item[1]<min:
                min=item[1]
        else:
            break
    r.sort()
    r=list(map(str,r))
    file.write(str(min)+'\n')
    file.write(' '.join(r))
