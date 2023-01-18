def uniquetester(s):
    i=0
    while i<len(s)-1:
        if s[i]==" ":
            i+=1
        j=i+1
        while j<len(s):
            if s[j]==" ":
                j+=1
            
            
            elif s[i]==s[j]:
                return False
            j+=1
        i+=1
    
    return True
    
    
print(uniquetester("am i unyqe"))