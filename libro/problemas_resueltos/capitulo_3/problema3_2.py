# El programa imprime y suma los términos de una serie.
BAND = 'T'
SUMSER = 0
i = 2
while(i <= 1800):
    SUMSER = SUMSER + i
    print(i)
    if BAND == 'T':
        BAND = 'F'
        i = i + 3
    else:
        BAND = 'T'
        i = i + 2
else:
    print(f"Los terminos en total de la serie son { SUMSER }")
print("Fin del programa")    
