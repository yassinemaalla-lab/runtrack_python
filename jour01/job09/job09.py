
nom = "souris"
prix_unitaire = 5
quantite_en_stock = 7
quantité_client = int(input("combien de souris voulez vous ?"))
quantite_en_stock = quantite_en_stock - quantité_client
prix_ajour = prix_unitaire * 1.10

print(f"votre {nom}   a eu une augumentation de 10% ce qui vous fait { prix_ajour} il reste {quantite_en_stock} exemplaires")
