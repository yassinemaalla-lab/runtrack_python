def calculerprix(nb_billets,prix_unitaire):
    return nb_billets * prix_unitaire
def passercommande():
    a = int (input("nombre de billet"))
    b = float (input("le prix d'un seul billet"))
    return calculerprix(a,b) 

total_apayer = passercommande()
if total_apayer >= 50 :
    print("tarif groupe")
else :
    print("tarif normal")

    