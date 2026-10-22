L = [8, 24,48,2,16]
L2 =[]
cpt = 0
for i in L:
    if i % 3 == 0 :
        L2.append(i)
        cpt += 1

print(f"il y a {cpt} multiples de 3 dans {L} ")
print(L2)