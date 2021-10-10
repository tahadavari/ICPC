# link : https://codeforces.com/problemset/problem/490/A
# sorting

n = int(input())

d = {index+1: i for index, i in enumerate(list(map(int, input().split())))}

d1 = {index: value for index, value in d.items() if value == 1}
d2 = {index: value for index, value in d.items() if value == 2}
d3 = {index: value for index, value in d.items() if value == 3}

team = min(len(d1), len(d2), len(d3))
print(team)
for i in range(team):
    print(list(d1.keys())[i],list(d2.keys())[i],list(d3.keys())[i])