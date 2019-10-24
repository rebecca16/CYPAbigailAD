#El programa obtiene el mayor y menornde N números enteros que se ingresan.
MAY = -100000
MEN = 100000
N = int(input("El numero de enteros que se ingresan son: "))
i = 1
NUM = 0
for i in range(1 , N , 1):
    NUM = (1 <= i <= N)
    if NUM > MAY:
        MAY = NUM
        if NUM < MEN:
            MEN = NUM
            i = i + 1
print(f"el numero mayor es: {MAY} y el numero menor es {MEN}")            


