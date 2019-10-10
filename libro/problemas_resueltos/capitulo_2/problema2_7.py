#El programa dados como datos tres números enteros, determina si los mismo están en orden creciente.
A = int (input("Ingresa un numero entero: "))
B= int (input("Ingresa un numero entero: "))
C = int (input("Ingresa un numero entero: "))
if A < B :
    if B < C :
        print(f"Los numeros estan en orden creciente")
    else:
        print(f"Los numeros no estan en orden creciente")
else:
    print(f"Los numeros no estan en orden creciente")
print(f"Fin del programa")    
