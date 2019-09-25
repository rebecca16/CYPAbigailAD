# El programa dado como dato el sueldo de un trabajador, le aplica un aumneto del 15% si su sueldo es inferior a $1000 y 12% en caso contrario
SUE = float (input("Ingresa tu sueldo:$ "))
if SUE < 1000:
    NSUE = SUE * 1.15
else:
    NSUE = SUE * 1.12
print (f"Tu sueldo es:$ {NSUE }")

