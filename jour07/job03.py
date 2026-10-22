def carte(n):
    for i in range(n):
        if i  == 0 or i == (n-1):
            print("+" + "-" * n + "+"  )
        else :
            ligne = ""
            for j in range(n):
                if j ==  i :
                    ligne += " "
                else :
                    ligne+= "#"

            print("|" + ligne + "|")
carte(13) 