# What is a list
# Usando el método de cadena "dividida" de la lección anterior, complete la función get_word para devolver la palabra {n} de una oración pasada.
# Por ejemplo, get_word("Esta es una lección sobre listas", 4) 
# debería devolver "lección", que es la cuarta palabra de esta oración. Sugerencia: recuerde que los índices de lista comienzan en 0, no en 1.

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split() #split retorna una lista de char: Ejemplo si la oracion es "This is a lesson about lists" => words = ['This','is', 'a','lesson','about','lists'] 
		# Only proceed if n is not more than the number of words 
		if n <= len(words): #solo considero los n menores a la cantidad de palabras.
			return(words[n-1]) # considerar que los arrays inician en el indice 0
	return("") # si el indice es negativo retorno un espacio 

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


#Modifying the Contentes of a Lista
# La función skip_elements devuelve una lista que contiene todos los demás elementos de una lista de entrada, comenzando con el primer elemento.
# Complete esta función para hacer eso, usando el bucle for para iterar a través de la lista de entrada.

def skip_elements(elements):
  # Initialize variables
  new_list = []
  i = 0
  
  # Iterate through the list
  for elements in elements:
    # Does this element belong in the resulting list?
    if i % 2 == 0:
      # Add this element to the resulting list
      new_list.append(elements)
    # Increment i
    i += 1

  return new_list

#List and Tuples
# Usemos tuplas para almacenar información sobre un archivo: su nombre, su tipo y su tamaño en bytes. 
# Complete los espacios en blanco en este código para devolver el tamaño en kilobytes (un kilobyte son 1024 bytes) hasta con 2 decimales.

def file_size(file_info):
	name, typefile, size = file_info #ojo con la palabra reservada type
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

# Iterating over Lists
# Pruebe la función de enumerar usted mismo en este ejercicio rápido. Complete la función skip_elements para devolver todos los demás elementos de la lista, 
# esta vez usando la función de enumerate para verificar si un elemento está en una posición par o impar

def skip_elements(elements):
	index = 0
	aux = [] #creo lista vacia auxiliar servira para agregar el contenido
	for index,elem in enumerate (elements): ##recorro lista, con la funcion enumerate existe la ventaja de no tener que usar un indice por fuera, 
        #ya que lo "crea" solo, index es el indice y elem es cada elemento de la lista
		if  check(index) == True: ##chequeo indices pares
			aux.append(elements[index]) #append inserta el contenido al final de la lista, con elements[index] accedo a los indices pares de la lista original y los transfiero al auxiliar
	return aux
 
def check(num): ##funcion auxiliar para chequear paridad
    if (num % 2) == 0:
        return True
    else:
        return False

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# List Comprehensions
#La función números_impares devuelve una lista de números impares entre 1 y n, ambos inclusive.
#  Completa los espacios en blanco de la función, usando la comprensión de listas.
# Sugerencia: recuerde que los contadores de lista y rango comienzan en 0 y terminan en el límite menos 1.

def odd_numbers(n):
	return [x for x in range (1,n+1,2)]
print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []