# El programa imprime y suma los términos de una serie.
SUMSER = 0
I = 2
BAND = str(input("Ingresa t o f: "))
f = 0
t = 0
while(I <= 1800):
    SUMSER = SUMSER + I
    if BAND == f:
        BAND == t
        I = I + 3
    else:
        BAND == t
        I = I + 2
        
print(SUMSER)
print("Fin del programa")
