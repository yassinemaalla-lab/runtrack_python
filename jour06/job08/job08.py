L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91] 
L2 = []
somme = 0
for i in L :
    if i % 2 == 0:
        L2.append(i)
        somme += i
        
print(L2)
print(somme)
