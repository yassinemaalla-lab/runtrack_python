Liste = [5,2,7,4,5]
print(Liste)
print(Liste[1])
for i in range(len(Liste)) :
    if Liste[i] == Liste[3] : 
        Liste[3] = Liste[2] + Liste[4]
print(Liste)
print(Liste[-1])