dict={"a":30,"b":70,}
dict2={"b":60,"c":30}
dic={}
for i,j in dict,dict2.items():
    for h,k in dict2.items():
        if i==h:
            a=j+k
            dic[i]=a
        if i!=h:
            dic[i]=j
print(dic)