L = [10, 20,30, 20, 10, 50, 60, 40, 80, 50, 40]
L2 = []
for i in range (len(L)) : 
        if L[i] not in L2 :
               L2.append(L[i])
print(L2)