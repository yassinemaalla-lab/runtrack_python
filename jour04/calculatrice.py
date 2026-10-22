def soustraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def addition(num1, num2):
    return num1 + num2

def calcultarice():
    num1 = int(input("Entrez votre premier nombre : "))
    num2 = int(input("Entrez votre second nombre : "))
    operation = input("Choisissez un operateur (+, -, *, /) : ")
    
    if operation == "+":
        print(f"Résultat : {addition(num1, num2)}")
    elif operation == "-":
        print(f"Résultat : {soustraction(num1, num2)}")
    elif operation == "*":
        print(f"Résultat : {multiplication(num1, num2)}")
    elif operation == "/":
        print(f"Résultat : {division(num1, num2)}")
    else:
        print("Opérateur non valide !")

calcultarice()