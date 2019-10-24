MED = 0
CHI = 0
GRA = 0
N = int(input("Introduce el numero de ventas del vendedor: "))
for i in range(0, N , 1):
    v = float(input("Introduce la venta del vendedor: "))
    if v <= 200:
        CHI = CHI + 1
    elif v < 400:
        MED = MED + 1
    else:
        GRA = GRA + 1
else:
    print(f"El numero de ventas menores es a $200 son {CHI}, menores a $400 son {MED} y mayores de $400 son {GRA}")
print("Fin del programa")    
