for i in range(1,100) :
    if i == 0 or i == 1 :
        print("n'est pas premier")
    elif i // i == i or i // 1 == i :
        print("est premier")
print(i)