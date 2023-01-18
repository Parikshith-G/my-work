def oneaway(x,y)->bool:

    if abs(len(x)-len(y))>=2:
        return False
    if len(x)==len(y):    
        print("pk")   
        count=0
        i=0
        while i<len(x):
            if x[i]!=y[i]:
                count+=1
            if count>1:
                return False
            i+=1
        return True
    if len(x)!=len(y):
        x=sorted(x)
        y=sorted(y)
        
        if len(x)>len(y):#pale pil$
            print("i")
            count=0
            i=0
            while i<len(y) :#ppp ppe
                if x[i]==y[i]:
                    print()
                    i+=1
                else:
                    y.insert(i,"*")
                    break
                
            if len(x)!=len(y):
                y.append("*")
            print(x,y)
            i=0
            while i<len(x):
                if x[i]!=y[i]:
                    count+=1
                if count>1:
                    return False
                i+=1
            return True
        if len(x)<len(y):#pale pil
            count=0
                # print("hit")
            i=len(y)-len(x)
            while i>0:
                print("la")
                if x[i]==y[i]:
                    continue
                else:
                    x.insert(i-1,"*")
                    i-=1
            i=0
        while i<len(x):
                if x[i]!=y[i]:
                    count+=1
                if count>1:
                    return False
                i+=1
        return True
        
                   
# print(oneaway("pale","pie"))
print(oneaway("pales","pale"))
print(oneaway("pale","bale"))
print(oneaway("pale","bake"))
"""pale pele
fd=false
i1->s1->p s2-> p fd=false
i2-> s1->a i2->e


boolean oneEditReplace(String sl, String s2) 
{
    boolean foundDifference = false;
    for (int i= 0; i < sl.length(); i++) 
    {
        if (sl.charAt(i) != s2.charAt(i)) 
        {
            if (foundDifference) 
            {
                 return false; 
            }
        foundDifference = true;
        }
    }
    return true;
}

"""
