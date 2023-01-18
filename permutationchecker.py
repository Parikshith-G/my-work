def sorter(x,y):
    # len1,len2=len(x),len(y)
    x=sorted(x.lower())
    y=sorted(y.lower())
    i,j=0,0
    while i<len(x) and j<len(y):
        if x[i]==y[j]:
            i+=1
            j+=1
        else:
            break
    if i==len(x) and j==len(y):
        return True
    return False
print(sorter("Stringone","stringone"))
print(sorter("stringone","string1"))
            
        