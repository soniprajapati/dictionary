d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'c':400}
d={}
sum1=0
for i in d1:
    for j in d2:
        if i==j:
            sum1=d1[i]+d2[j]
            d.update({i:sum1})
            print(d)
            