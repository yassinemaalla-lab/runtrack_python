from job06 import signe
def verifier_nombre(nombre):
    if nombre % 2 == 0 :
        print("ce nombre est pair")
    else :
        print("ce nombre est impair" )
    signe(nombre)
verifier_nombre(-3)