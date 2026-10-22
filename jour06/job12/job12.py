L = [7, 11, 42, 39, 2]
for i in range(len(L)) :
    for j in range(i+1,len(L)) :
        if L[i] > L[j]:
           L[i],L[j] = L[j],L[i]
print(L)