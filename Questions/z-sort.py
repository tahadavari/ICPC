# link : https://codeforces.com/problemset/problem/652/B
# sorting 

def check(l):
    for i in range(len(l)):
        if (i+1)%2==0:
            if not l[i]>=l[i-1]:
                return False
        else:
            if not l[i]<=l[i-1]:
                return False
    return True



n = int(input())

l = [int(x) for x in input().split()]

l.sort()
# print (l)

result = [l[0]]
l.pop(0)

for i in range(1,len(l)+1):
    if (i+1)%2==0:
        result.append(l[-1])
        if not check(result):
            print('Impossible')
            break
        else:
            l.pop(-1)
        # print('even',result)
    
    else:
        result.append(l[0])
        if not check(result):
            print('Impossible')
            break
        else:
            l.pop(0)
        # print('odd',result)

else:
    print(*result)


        



