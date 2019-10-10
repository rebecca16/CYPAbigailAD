# El programa, dado como datos la matrícula yt calificaciones de un alumno; imprime la matrícula, el promedio y "aprobado" o"no aprobado", dependiendo si su promedio fue mayor o igual que 6 o menor que 6, respectivamente.
MAT = int(input("Ingresa tu matricula: "))
CAL1 = float(input("Ingresa tu calificacion: "))
CAL2 = float(input("Ingresa tu calificacion: "))
CAL3 = float(input("Ingresa tu calificacion: "))
CAL4 = float(input("Ingresa tu calificacion: "))
CAL5 = float(input("Ingresa tu calificacion: "))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5) / 5 
if PRO > 6 :
    print(f"Tu matricula es: { MAT }, tu promedio es: { PRO } y estas aprobado")
else:
    print(f"Tu matricula es: { MAT }, tu promedio es: { PRO } y estas reprobado")
print(f"Fin del programa")    
