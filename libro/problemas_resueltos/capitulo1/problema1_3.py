# El programa, dado el nombre de un dinosaurio su peso expresado en toneladas y su longitud expresada en libras; escribe el nombre del dinosaurio, su peso y longitud expresadas en kilogramos y metros, respectivamente
NOM = str (input("Introduce el nombre de un dinosaurio "))
PES = float (input("Introduce el peso en libras del dinosaurio "))
LON = float (input("Introduce la longitud en pies del dinosaurio "))
PESKIL = PES * 1000
LONMET = LON * .3047
print(f"El peso del dinosaurio en kilogramos es: { PESKIL }kg y la longitud en metros es: { LONMET }mts")
