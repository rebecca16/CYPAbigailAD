# el programa, dado como datos el radio y la altura de un cilindro, calcula su área y su volumen.
ALTU = float (input("Ingresa la altura de tu cilindro: "))
RADIO = float (input("Ingresa el radio de tu cilindro: "))
VOL = 3.141592 * (RADIO ** 2) * ALTU 
ARE = 2 * 3.141592 * RADIO * ALTU
print (f"El volumen de tu cilindro es: { VOL } y el area de tu cilindro es: { ARE }")
