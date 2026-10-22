def calculer_ttc(prixht,tva):
    prix_ttc = prixht + (prixht * tva)/100
    return prix_ttc
def demander_et_calculer():
    a = float(input("donner moi votre prix ht"))
    b = float(input("le taux de votre tva"))
    return calculer_ttc(a,b)
prix_final = demander_et_calculer()
if prix_final > 100 :
    print("livraison gratuite")
else :
    print("frais de port 5 euros ")
    

