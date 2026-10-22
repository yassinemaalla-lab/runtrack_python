def est_majeur(age):
    age = int (input("entre un age "))
    if age >= 18 :
        return True
    else : 
        return False
resultat = est_majeur
print(est_majeur(20))