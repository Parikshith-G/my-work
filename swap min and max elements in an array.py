def converterfromdecimal(num,base):
    if base=="bina":
        ans=""
        while num>0:
            ans+="".join(str(num%2))
            num//=2
        return ans[::-1]
    
    if base=="octal":
        ans=""
        while num>0:
            ans+="".join(str(num%8))
            num//=8
        return ans[::-1]
    if base=="hexa":
        ans=""
        while num>0:
            k=num%16
            if k==10:
                ans+="".join("A")
            elif k==11:
                ans+="".join("B")
            elif k==12:
                ans+="".join("C")
            elif k==13:
                ans+="".join("D")
            elif k==14:
                ans+="".join("E")
            elif k==15:
                ans+="".join("F")
            elif k==16:
                ans+="".join("G")
            else:
                ans+="".join(str(num%16))
                
                
            
            num//=16
        return ans[::-1]
        
    
print(converterfromdecimal(123456789,"hexa"))