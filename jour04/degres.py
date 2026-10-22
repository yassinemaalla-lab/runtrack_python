def verifier_age() :
    nombre = int(input("entrez votre age "))
    if nombre < 18 :
        print("mineur")
    elif nombre < 65 :
        print ("majeur")
    else :
        print("senior")
verifier_age()
    
