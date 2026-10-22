from random import randrange

def lancer_jeu():
    # 1. On génère le nombre aléatoire avant la boucle (entre 1 et 100 inclus)
    nombre_mystere = randrange(1, 101)
    tentative_restante = 3


    print("Bienvenue dans le jeu du nombre mystère !")

    # 2. La boucle dépend de la variable tentative_restante
    while tentative_restante > 0:
        choix_user = int(input("Entrez votre numéro : "))

        if choix_user == nombre_mystere:
            print("Bravo, vous avez trouvé !")
            return  # Sort immédiatement de la fonction (et donc de la boucle)

        elif choix_user > nombre_mystere:
            print("Votre numéro est trop grand.")
        else:
            print("Votre numéro est trop petit.")

        # On retire une tentative après chaque erreur
        tentative_restante -= 1
        print(f"Tentatives restantes : {tentative_restante}\n")

    # 3. Si la boucle se termine sans victoire
    print(f"Vous avez perdu ! Le nombre mystère était {nombre_mystere}.")

# Lancer la partie
lancer_jeu()
    
