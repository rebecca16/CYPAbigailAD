NUM = int(input("Ingresa un numero entero psoitivo "))
V = int(input("Ingresa otro numero entero positivo "))
if NUM == 1 :
    VAL = 100 * V
    print(f" { VAL }")
elif NUM == 2 :
    VAL = 100 ** V
    print(f" { VAL }")
elif NUM == 3 :
    VAL = 100 / V
    print(f"{ VAL }")
else:
    VAL = 0
    print(f"{ VAL }")
print(f"Fin del programa")    

