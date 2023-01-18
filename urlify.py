def urlify(x):
    ans=[]
    for i in range(len(x)):
        
        if x[i]==" ":
            ans.append("%20")
            
        else:
            ans.append(x[i])
    return "".join(ans)


print(urlify("Mr 3ohn Smith"))