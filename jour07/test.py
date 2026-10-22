def nombre_marche(x,y):
    marchemettre = x 
    hauteurmettre = y 
    calculmarche = marchemettre * (hauteurmettre )* 2  / 100
    nombre_jour = calculmarche * 5 
    nombresemaine = nombre_jour * 7
    print(
        f"Pour {x} marches de {y} cm, le gardien parcourt"
        f" {nombresemaine:.2f} m par semaine.")
(nombre_marche(100,20))