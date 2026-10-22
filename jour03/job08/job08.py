a = int(input("entrez la premiere longueur : "))
b = int(input("entrez deuxieme longueur : "))
c = int(input("entrez troisieme longueur : "))

a, b, c = sorted([a, b, c])

if a + b < c:
    print("ne peut pas etre un triangle")
elif a + b == c:
    print("est un triangle a plat")
else:
    if a == b and b == c:
        print("triangle equilateral")
    elif (a * a) + (b * b) == c * c:
        if a == b or b == c or a == c:
            print("C'est un triangle rectangle et isocele")
        else:
            print("C'est un triangle rectangle")
    elif a == b or b == c or a == c:
        print("est un triangle isocele")
    else:
        print("un triangle quelconque")