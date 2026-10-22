chaine = "abcdefghijklmonp"
chaine1 = ""
for i in range(len(chaine)):
    if chaine[i]== chaine[i].lower():
        chaine1 += chaine[i].upper()
    else :
        chaine1 += chaine[i]

print(chaine1)