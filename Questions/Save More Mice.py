for tc in range(int(input())):
    k, n = map(int, input().split())
    l = [int(x) for x in input().split()]
    l.sort()
    mosh = 0
    gorbe = 0
    while l:
        l[-1] += 1
        if l[-1] == k:
            l.pop(-1)
            mosh += 1
        gorbe +=1
        while True and l:
            if gorbe==l[0]:
                l.pop(0)
            else:
                break
  
    print(mosh)