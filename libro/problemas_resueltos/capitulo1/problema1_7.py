L1 = float (input("Ingresa el primer lado de tu triangulo: "))
L2 = float  (input("Ingresa el segundo lado de tu triangulo: "))
L3 = float (input("INgresa el tercer lado de tu triangulo: "))
S = (L1 + L2 + L3)/2
AREA = (S * (S - L1) * (S - L2) * (S - L3)) ** 0.5
print (f"El area es : { AREA }")

