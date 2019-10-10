A = int (input("Ingresa un numero entero: "))
B = int (input("Ingresa un numero entero: "))
C = int (input("Ingresa un numero entero: "))
if A > B :
    if A > C :
        print(f" {A} es el mayor")
    else:
        if A == C :
            print("{A} y {C} son los mayores")
        else:
            print(f"{C} es el mayor")
else:
    if A == B :
        if A > C :
            print(f"{A} y {B} son los mayores")
        else:
             if A == C :
                print(f"{A}, {B} y {C} son los mayores")
             else:
                print(f"{C} es el mayor")
    else:
         if B > C :
             print(f"{B} es el mayor")
         else:
             if B == C :
                 print(f"{B} y {C} son los mayores")
             else:
                 print(f"{C} es el mayor")
print(f"fin del programa")                 




