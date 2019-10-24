#El programa calcula el resultado de una determinada serie.
SERIE = 0
N = int(input("Ingresa un numero de tipo entero: "))
BAND = 'T'
i = 1
for i in range(1 , N , 1):
    if BAND == 'T':
        SERIE = SERIE + 1 / 1
        BAND = 'F'
    else:
        SERIE = SERIE - 1 / i
        BAND = 'T'
else:
    print(f"El resultado es: {SERIE}")

print("Fin del programa")
        
