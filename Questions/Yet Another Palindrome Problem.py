# link : https://codeforces.com/group/yoISfMyBdK/contest/344724/problem/D

import itertools
def palindrome (STR):
    if STR == STR[::-1]:
        return True
    return False

def Sub_Sequences(STR):
    combs = []
    for l in range(1, len(STR)+1):
        combs.append(list(itertools.combinations(STR, l)))
    for c in combs:
        for t in c:
            if len(t)>=3 and palindrome(t):
                yield ''.join(t)
    del combs



tc = int(input())
for i in range(tc):
    n = int(input())
    num = ''.join(list(input().split()))
    sub = list(Sub_Sequences(num))
    if sub:
        print('YES')
    else:
        print('NO')
    del sub

    