def uniquetester(s):
    d={}
    for index,value in enumerate(s):
        if value==" ":
            continue
        if  value in d:
            
            return False
        d[value]=index
    
    return True
    
    
print(uniquetester("am i uniyqe"))