CATE = int(input("EScoge la categoria de empleado del 1_4 "))
SUE = float(input("Ingresa tu sueldo"))
if CATE == 1 :
    NSUE = SUE * 1.15
    print(f"Su nuevo sueldo es: { NSUE } y la categoria es { CATE }")
elif CATE == 2 :
    NSUE = SUE * 1.10
    print(f"Su nuevo sueldo es: { NSUE } y la categoria es { CATE }")
elif CATE == 3 :
    NSUE = SUE * 1.08
    print(f"Su nuevo sueldo es: { NSUE } y la categoria es { CATE }")
elif CATE == 4 :
    NSUE = SUE * 1.07
    print(f"Su nuevo sueldo es: { NSUE } y la categoria es { CATE }")
else:
    print(f"Su valor no es valido")
print(f"Fin del programa")    
