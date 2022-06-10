# Whats is a dictionary
# El diccionario "toc" representa la tabla de contenido de un libro. 
# Llene los espacios en blanco para hacer lo siguiente: 
# 1) Agregue una entrada para el Epílogo en la página 39. 
# 2) Cambie el número de página del Capítulo 3 a 24.
#  3) Muestre los nuevos contenidos del diccionario. 
#  4) Muestre Verdadero si hay Capítulo 5, Falso si no lo hay.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc ["Epilogue"] = 39   # Agrego elemento Epilogue starts on page 39 
toc ["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?

# Iterating over the Contents of a Dictionary

# ¡Ahora es tu turno! ¡Prueba a iterar sobre un diccionario! Complete el código para iterar a través de las claves y valores del diccionario cool_beasts.
#  Recuerde que el método de elementos devuelve una tupla de clave, valor para cada elemento en el diccionario

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast,part in cool_beasts.items(): # beast, part son la clave y el valor de cada tupla que retorna el metodo items() 
    print("{} have {}".format(beast,part)) #imprimo

# Dictionaries vs. Lists

# En Python, un diccionario solo puede contener un único valor para una clave dada. Para solucionar esto, nuestro valor único puede ser una lista
#  que contenga varios valores. Aquí tenemos un diccionario llamado "vestuario" con prendas de vestir y sus colores. 
# Complete los espacios en blanco para imprimir una línea para cada prenda con cada color, por ejemplo: "camisa roja", "camisa azul", etc.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for prenda,lista_color in wardrobe.items():
	for color in lista_color:
		print("{} {}".format(color,prenda))