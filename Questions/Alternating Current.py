

def r(sim):
    if sim==[]:
        return True
    flag =False
    for i in range(len(sim)-1):
        if sim[i]==sim[i+1]:
            sim.pop(i)
            sim.pop(i)
            flag = True
            break
    if flag:
        return r(sim)
    else:
        return False
    
    
sim = list(input())

print('Yes' if r(sim) else 'No')