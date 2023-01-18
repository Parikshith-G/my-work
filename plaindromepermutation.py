def palindromepremutation(x):
    x=x.lower()

    tester=[]
    for i in x:
        if i==" ":
            continue
        tester.append(i)
    tester.sort()
    
    res=[]
    i,j=0,1
    while j<len(tester):
        if tester[i]==tester[j]:
            i+=2
            j+=2
        elif tester[i]!=tester[j]:
            
            res.append(x[j])
            i+=2
            j+=2
    if len(res)==0 or len(res)==1:
        return True
    return False
            
        
        
    

print(palindromepremutation("malalaplalam"))