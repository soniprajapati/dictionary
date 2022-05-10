list= "w3recource"
dic= {}
  
for i in list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print (str(dic))
                                        