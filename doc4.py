n=int(input("enter:"))
dic={}
for i in range (1,n):
    dic.update({i:i*i})
print(dic)