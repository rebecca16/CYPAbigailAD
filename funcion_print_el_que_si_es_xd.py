# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- con la funcion format ()
4.- Es con una variante de format ()
"""
# Con comas
#un espacio y haciendo casting de tipo 
edad = 10
nombre = "Juan"
estatura = 1.67
print (edad , estatura , nombre )

# con '+' hace lo mismo pero no realiza el casting automático
# no agrega espacio, todo va a aparecer junto

print (str(edad) + str(estatura) + nombre )

# funcion format ()

print("nombre: {} edad: {} ".format(nombre, edad, estatura))

# la la 4.- es con una variante de format() simplificada

print(f"nombre: \"{nombre}\" \nedad:\t{edad} ")

# print y el argumento end

print("Solo hay diez tipos de personas, las que saben binario y las que no",end="------ ")
print("Otra linea")

