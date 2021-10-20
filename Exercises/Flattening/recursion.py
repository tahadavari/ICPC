def flatten(L):
    
    if len(L) == 1:
        
            if type(L[0]) == list:
                
                    result = flatten(L[0])
                    
            else:
                
                    result = L
                
    elif type(L[0]) == list:
        
            result = flatten(L[0]) + flatten(L[1:])
            
    else:
        
            result = [L[0]] + flatten(L[1:])
        
    return result

print(flatten([1,[4,[3,4]]]))