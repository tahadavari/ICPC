# link : https://codeforces.com/group/yoISfMyBdK/contest/344724/problem/C

n1  = list(input())
n2 = list(input())
y = list(str(int(''.join(n1)) + int(''.join(n2))))
while True:
    try:
        y.remove('0')
    except :
        break
while True:
    try:
        n1.remove('0')
    except :
        break
while True:
    try:
        n2.remove('0')
    except :
        break

x = int(''.join(n1)) + int(''.join(n2))
y = int(''.join(y))
print ('YES') if x==y else print('NO')