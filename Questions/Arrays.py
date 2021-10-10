# link : https://codeforces.com/problemset/problem/572/A
# sorting

nA,nB = map(int,input().split())

k,m = map(int,input().split())

A = [int(x) for x in input().split()][:k]
B = [int(x) for x in input().split()][nB-m:]

print('YES') if A[k-1]<B[0] else print("NO")

            

