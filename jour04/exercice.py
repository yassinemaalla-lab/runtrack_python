def moyenne(note1,note2):
    return (note1 + note2 ) / 2



def afficher_resultat():
    a = float(input("note1 " ))
    b = float(input("note2 "))

    print(f"voila {moyenne(a,b)} est la moyenne")
    return moyenne(a,b)

afficher_resultat()

# moyenne_final = afficher_resultat()
# if moyenne_final > 10 :
#     print("admis")
# else :
#     print("rattrapage")

