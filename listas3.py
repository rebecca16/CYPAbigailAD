autos=["Akura","Mazda","Honda","Toyota","Nissan"]
motos=["Ducati","Kawasaki","Harley Davidson","BMW","Italika"]
bicis=["Bennoto","BMX","Apache","Mercurio","Trek"]
vehiculos=[autos,motos,bicis]

print(motos[2])
print(vehiculos[1][2])
print(vehiculos[2][4])
print(autos[1:4:1]) #Slicing (1(es donde empieza):4(el tope pero no se muestra):1(de cuanto en cuanto va)).
print(motos[-2:-5:-1]) #El -1 invierte el orden de la lista.
print(bicis[::-1]) #No se ponen los úmeros porque ya se dan por entendio el tope y que es inverso.
print(vehiculos[2][1:4:1])
print(vehiculos[1::])
