#Arreglos
#Lectura
# escritura/asignación
#actualización : inserción, eliminación , modificación
#ordenamiento
#busqueda

#escritura
frutas = ["Zapote","Manazana", "Pera", "Aguacate", "Durazno" , "Uva","Sandía"]

#lectura, el selector [ indice ]
print(frutas[2])

#lectura con for
#for opción 1
for indice in range(0,7,1):
    print(frutas[indice])
print("------")

# for opcion 2 -- por un iterador for each

for fr in frutas:
    print(fr)

# asignación
frutas[2]="Melón"
print(frutas)

#inserción al final
frutas.append("Naranja")
print(frutas)
print(len(frutas))
frutas.insert(2,"Limon")
print(len(frutas))
frutas.insert(0,"Mamey")
print(frutas)

# eliminación con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas[2]="limon"
frutas.append("limon")
frutas.append("limon")
print(frutas)
frutas.remove("limon")
print(frutas)

# ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

# busqueda
print(f"La uva esta en la posicion { frutas.index('Uva') } ") 

print(f"El limon esta {frutas.count('limon') } veces en la lista")

# concatenar
print(frutas)
otras_frutas = ["Rambutan","Nispero","Liche","Pitahaya"]
frutas.extend(otras_frutas)
print(frutas)

# copiar
copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia = frutas.copy()
otra_copia.append ("Fresa")
otra_copia.append ("Fresa")
print(frutas)
print (otra_copia)
