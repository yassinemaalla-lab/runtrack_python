def time_totext(nombre):
        heure = nombre // 60
        minute = nombre % 60
        print(f"le resultat est de {heure}h et {minute} minutes")
time_totext(int (input("entrez un nombre")))