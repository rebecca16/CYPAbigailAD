#El programa dado como dato un número entero, dtermina si el mismo es positivo, negativo o nulo.
NUM = int(input("Ingresa un numero entero: "))
if NUM > 0 :
    print(f"El numero { NUM } es psotivo")
elif NUM == 0 :
    print(f"El numero { NUM } es nulo")
else:
    print(f"El numero { NUM } es negativo")
print(f"Fin del programa")    
