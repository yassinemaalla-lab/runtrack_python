def triangle(hauteur):
    i = 0
    while i < hauteur :
        if i == hauteur-1 or i == 0 :
            print("/" + "-"  * i + "\\" )
        else :
            print("/" + " "  * i + "\\") 
        i+= 1
triangle(10)