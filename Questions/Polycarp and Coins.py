for tc in range(int(input())):
    n = int(input())
    i = 1
    if n%3==0:
        i = 0
    a = n//3
    b = (n//3) +i
    if (b*2) + a == n:
        print(a,b)
    else:
        print(b,a)