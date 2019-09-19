# El programa, dado como datos la base y la altura de un rectangulo, calcula su perimetro y superficie 
BASE = float (input("Introduce la base de tu rectangulo"))
ALTU = float (input("Introduce la altura de tu rectangulo"))
SUP = BASE * ALTU
PER = 2 * (BASE + ALTU)
print (f"La superficie de tu rectangulo es { SUP }")
print (f"El perimetro de tu rectangulo es { PER }")
