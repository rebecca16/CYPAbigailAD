#El programa dado como dato un número entero, determina si el mismo es par, impar o nulo.
A = int(input("Ingresa un numero entero: "))
if A == 0 :
    print(f"El numero { A } es nulo")
elif (-1 ** A) > 0 :
    print(f"El numero { A } es par")
else:
    print(f"El numero { A } es impar")
print(f"Fin del programa")    

