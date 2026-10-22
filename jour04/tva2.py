def calculer_ttc(prixht,tva):
    return prixht +(prixht * tva)/100
def afficher_facture(montant_ttc) :
    print(f"le total a payer est de {montant_ttc}euro")
    if montant_ttc > 100 :
        print("livraison gratuite")
    else :
        print("frais de port de 5 euro ")
prixht = float (input("votre prix ht"))
tva = float(input("votre tva"))
calculer_ttc(prixht,tva)
total = calculer_ttc(prixht,tva)
afficher_facture(total)