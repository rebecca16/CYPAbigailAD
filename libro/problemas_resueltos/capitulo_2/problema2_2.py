#El programa dado como datos dos valores enteros, determina si los mismos satisfacen una expresión.
P = int(input("Ingresa un numero entero: "))
Q = int(input("Ingresa otro numero entero: "))
EXP = P ** 3 + Q ** 4 - 2 * P ** 2
print(f"El resultado es: { EXP }")
if EXP < 680 :
    print(f" { P } y { Q } no satisfacen la expresion")
print(f"Fin del programa")    
