#El programa, teniendo en cuenta ciertos criterios, calcula el aumento de sueldo para un grupo de trabajadores. Imprime el nuevo sueldo del trbajador y la nómina correspondiente.
NOM = 0
SUE = 0
while( SUE != (-1)):
    if SUE < 1000:
        NSUE = SUE*1.15
    else:
        NSUE = SUE*1.2
    NOM = NOM + NSUE
    print(f"El nuevo sueldo del trabajador es ${NSUE}")
    SUE = float(input("Introduce el sueldo del trabajador: "))
else:
    print(f"El nuevo sueldo de los ytrabajadores es ${NOM}")

print("Fin del programa")    

