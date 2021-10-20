l = [1,[2,[3,4]],[1,7]]

flat = []
    
while l: #runs until the given list is empty.
    
        e = l.pop(0)
        
        if type(e) == list: #checks the type of the poped item.
            
                l.extend(e) #if list extend the item to given list.
        else:
            
                flat.append(e) #if not list then add it to the flat list.
        
print(flat)