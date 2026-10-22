L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
min = L[0]
max = L[0]
for i in L :
    if min > i + 1 :
        min = i 
    if max < i + 1 :
        max = i
print(f"la valeur minimale est : {min}")
print(f"la valeur maximale est : {max}")

