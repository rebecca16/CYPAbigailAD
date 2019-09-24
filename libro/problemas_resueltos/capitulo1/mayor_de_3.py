NUM1 = float (input("Ingresa el primer numero: "))
NUM2 = float (input("Ingresa el segundo numero: "))
NUM3 = float (input("Ingresa el tercer numero: "))

if NUM1 < NUM2 and NUM2 < NUM3:
    print (f"{NUM3} es el numero mas grande")
if NUM1 > NUM2 and NUM2 > NUM3:
    print (f"{NUM1} es el numero mas grande")
if NUM1 < NUM2 and NUM2 > NUM3:
    print (f"{NUM2} es el numero mayor")
print ("Fin del programa")        

