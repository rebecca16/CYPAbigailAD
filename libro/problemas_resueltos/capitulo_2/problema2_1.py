# El programa, dado como dato el númerode sonidos emitidos por un grillo en un minuto, calcula la temperatura en grados Farenheith.
N = float(input("Ingresa el numero de sonidos emitidos por el grillo en un minuto: "))
if N > 0 :
    T = N / 4 + 40
    print(f"La temperatura es: { T }")
print(f"Fin del programa")    
