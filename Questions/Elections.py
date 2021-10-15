for tc in range(int(input())):
    a,b,c=map(int,input().split())
    m = max(a,b,c)
    l=[a,b,c]
    if l.count(m)==1:
        if a==m:
            a+=1
        if b==m:
            b+=1
        if c==m:
            c+=1
    print((m-a)+1,(m-b)+1,(m-c)+1)