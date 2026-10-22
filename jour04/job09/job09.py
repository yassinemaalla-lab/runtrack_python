def moyenne(a,b,c):
    resultat = (a + b + c)/3
    return resultat
def moyen():
    a = float(input("entrez votre 1 note : "))
    b =  float(input("entrez votre 2 note : "))
    c =  float(input ("entrez votre 3 note : "))
    return moyenne(a,b,c)
moyenne_etudiant = moyen()
print(f"Votre moyenne est de : {moyenne_etudiant :.2f}")

if moyenne_etudiant >= 15  :
    print(" très bon eleve !")
elif moyenne_etudiant >= 11 :
    print("bon eleve.")
elif moyenne_etudiant >= 8  :
    print("eleve moyen")
else:
    print("Il faut encore travailler.")