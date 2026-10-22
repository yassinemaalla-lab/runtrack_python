def dessin(width,height):
    i = 0
    while i < height :
        if i == 0 or i == height -1 :
            print("|" + '-' * (width-2) +"|")
        else :
            print("|"+ " " * (width-2)+'|')
        i+=1
dessin(6,3)
    