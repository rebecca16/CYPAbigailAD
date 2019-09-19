# El algoritmo, dadas cinco calificaciones de un alumno, calcula su promedio
MAT = str (input("Introduce el nombre de tu materia "))
CAL1 = float (input("Introduce tu primer calificacion "))
CAL2 = float (input("Introduce tu segunda calificacion "))
CAL3 = float (input("Introduce tu tercer calificacion "))
CAL4 = float (input("Introduce tu cuarta calificacion "))
CAL5 = float (input("Introduce tu quinta calificacion "))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
print (f"El nombre de tu materia es { MAT }")
print (f"Tu promedio es { PRO }")

