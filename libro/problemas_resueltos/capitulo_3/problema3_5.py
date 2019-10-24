#El programa dado N números enteros como dato, obtiene el número de números psotitvos, el promedio de los números positivos y el promedio de todos los números.
SUMPOS = 0.0
CUEPOS = 0
SUMOTR = 0
N = int(input("Ingresa la cantidad de datos que vas a ingresar: "))
for i in range(0 , N , 1):
    NUM = int(input("Introduce un numero entero: "))
    if NUM > 0:
        SUMPOS = SUMPOS + NUM 
        CUEPOS = CUEPOS + 1
    else:
        SUMOTR = SUMOTR + NUM
else:
    PROGEN = (SUMPOS + SUMOTR) / N
    PROPOS = SUMPOS / CUEPOS
    print(f"Los numeros positivos son: { CUEPOS }, el promedio de numeros positivos es: { PROPOS } y el promedio general de los numeros es: { PROGEN }")
print("Fin del programa")
