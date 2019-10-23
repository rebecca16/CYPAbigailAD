# El rpograma dados 270 números enteros, obtiene la suma de los números impares y el promedio de los números pares.
i = 0
num = 0
SUMPAR = 0
SUMIMP = 0
CUEPAR = 1
for i in range(1 , 11 , 1):
    num = int(input("Ingresa un numero entero: "))
if num > 0 :
    if (-1 ** num) > 0:
        SUMPAR = SUMPAR + num 
        CUEPAR = CUEPAR + 1
    else:
        SUMIMP = SUMIMP + num
i = i + 1
PROPAR = SUMPAR / CUEPAR
print(f" El promedio de numeros pares es: { PROPAR } y los numeros impares son: { SUMIMP }")

