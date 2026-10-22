def convertir_endollars(euro,taux):
    dollars = euro * taux
    return dollars
def saisir_etconvertir():
    a = float(input("entrez votre somme"))
    b =  float (input("entrez votre taux"))
    return convertir_endollars(a,b)
some_final = saisir_etconvertir()
if some_final < 1000 :
    print("kdkd")

else :
    print("gghhhh")