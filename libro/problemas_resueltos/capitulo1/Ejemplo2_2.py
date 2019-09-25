# El programa dado como dato el sueldo de un trabajador, le aplica un aumneto del 15% si su sueldo es inferior a $1000
SUE = float (input("Ingresa tu sueldo: "))
if SUE < 1000:
    AUM = SUE * 0.15
    NSUE = SUE + AUM
    print (f" Tu sueldo con el aumento es: { NSUE } ")
else:
    print (f" Fin del programa")
