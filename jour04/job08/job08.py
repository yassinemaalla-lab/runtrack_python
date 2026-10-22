def fruitetlegumes(type,saison):
    if type == "fruit" and saison == "hiver" :
        print("orange, mandarine et kiwi,")
    elif type == "fruit" and saison == "ete" :
        print(" Poire, fraise, cassis")
    elif type == "legumes" and saison == "ete":
        print("carotte, topinambour, endive")
    else :
        print("« artichaut, aubergine,navet")
fruitetlegumes("fruit","hiver")
fruitetlegumes("legumes","ete")
