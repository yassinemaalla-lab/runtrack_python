def voyelle(text):
    cpt = 0
    for i in text :
        if i in "aeiouy":
            cpt += 1
    return cpt 
print(f"il y a {cpt} dans {text}")
voyelle("hello")
