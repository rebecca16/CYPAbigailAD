#El programa dados como datos tres números enteros, determina si los mismo están en orden creciente.
A = int(input("Ingresa un numero entero: "))
B= int(input("Ingresa un numero entero: "))
C = int(input("Ingresa un numero entero: "))
if A < C :
    if B < C :
        print(f"Los numeros de manera creciente quedan asi: {A},{B},{C}")
    else:
        print(f"Los numeros de manera creciente quedan asi: {B},{A}.{C}")
else:
    if  
