#El programa, dado como datos los coeficientes de la ecuación, calcula las raices reales -si existen-.
A = float(input("Ingresa un coeficiente: "))
B = float(input("Ingresa un coeficiente: "))
C = float(input("Ingresa un coeficiente: "))
DIS = (B ** 2) - 4 * A * C
print(f"El resultado es: { DIS }")
if DIS > 0 :
    X1 = ((-B) + DIS ** 0.5) / 2 * A
    X2 = ((-B) - DIS ** 0.5) / 2 * A
    print(f"Las raices reales son: { X1 } y { X2 }")
print(f"Fin del programa")    
