def calcul(a,operateur,b):
    #a = int(input())
    #b = int(input())
    res = int
    if operateur == "+":
        res = a + b
    elif operateur == "-":
        res =  a - b
    elif operateur == "%":
        res= a % b 
    elif operateur == "/":
        res = a // b
    else :
        res = a * b
    return res
    
print(calcul(5,'-',6))