def calculer_surface(longueur,largeur):
    return longueur * largeur 
def demander_dimensions():
    a = float (input("votre longueur "))
    b = float(input("votre largeur"))
    return calculer_surface(a,b)
surface_totale = demander_dimensions()
if surface_totale >= 50 :
    print("surface grande")
else :
    print("surface petite")