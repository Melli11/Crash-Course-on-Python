# Pregunta 1
# La función format_address separa partes de la cadena de dirección en nuevas cadenas: house_number y street_name, y devuelve: "house number X on street named Y".
# El formato de la cadena de entrada es: número de casa numérico, seguido del nombre de la calle que puede contener números, pero nunca solos, y puede tener varias
# palabras. Por ejemplo, "123 Main Street", "1001 1st Ave" o "55 North Center Drive". 
# Rellena los huecos para completar esta función.

# def format_address(address_string):
#   # Declare variables

#   # Separate the address string into parts

#   # Traverse through the address parts
#   for __:
#     # Determine if the address part is the
#     # house number or part of the street name

#   # Does anything else need to be done 
#   # before returning the result?
  
#   # Return the formatted string  
#   return "house number {} on street named {}".format(__)

# print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

# print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

# print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

#Pregunta 2
# La función Highlight_word cambia la palabra dada en una oración a su versión en mayúsculas. 
# Por ejemplo, resaltar_palabra("Que tengas un buen día", "bueno") devuelve "Que tengas un BUEN día". ¿Puedes escribir esta función en una sola línea?


def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))
	
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#Pregunta 3
# Un profesor con dos asistentes, Jamie y Drew, quiere una lista de asistencia de los estudiantes, en el orden en que llegaron al salón de clases.
# Drew fue el primero en notar qué estudiantes llegaban y luego Jamie se hizo cargo.
# Después de la clase, cada uno ingresó sus listas en la computadora y las envió por correo electrónico al profesor, quien debe combinarlas en una sola,
#  en el orden de llegada de cada estudiante. 
# Jamie envió un correo electrónico de seguimiento, diciendo que su lista está en orden inverso.
#  Complete los pasos para combinarlos en una lista de la siguiente manera: 
# el contenido de la lista de Drew, seguido de la lista de Jamie en orden inverso, para obtener una lista precisa de los estudiantes cuando llegaron.

def combine_lists(list1, list2):
  list1.reverse()  # Generate a new list containing the elements of list2
  list2.extend(list1)# Followed by the elements of list1 in reverse order
  return list2
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


# Pregunta 4
# Usa una lista de comprensión para crear una lista de números cuadrados (n*n). La función recibe las variables inicio y fin,
#  y devuelve una lista de cuadrados de números consecutivos entre inicio y fin inclusive. 
# Por ejemplo, cuadrados (2, 3) debería devolver [4, 9].

def squares(start, end):
	x = start
	return [ x*x for x in range (start,end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Pregunta 5
# Complete el código para iterar a través de las claves y valores del diccionario car_prices, imprimiendo información sobre cada uno.
# def car_listing(car_prices):

def car_listing(car_prices):
  result = ""
  for model,price in car_prices.items():
    result += "{} costs {} dollars".format(model,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Pregunta 6
# Taylor y Rory organizan una fiesta. Enviaron invitaciones y cada uno recopiló respuestas en diccionarios, con los nombres de sus amigos
# y cuántos invitados traería cada amigo. Cada diccionario es una lista parcial, pero la lista de Rory
# tiene información más actualizada sobre el número de invitados. Complete los espacios en blanco para combinar ambos diccionarios en uno,
# con cada amigo enumerado solo una vez, y el número de invitados del diccionario de Rory tiene prioridad, si se incluye un nombre en ambos diccionarios.
# Luego imprima el diccionario resultante.

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  guests2.update(guests1)
  return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))


# Pregunta 7
# Use un diccionario para contar la frecuencia de las letras en la cadena de entrada. Solo se deben contar las letras, no los espacios en blanco,
#  los números ni la puntuación. Las mayúsculas deben considerarse lo mismo que las minúsculas.
# Por ejemplo, count_letters("Esta es una oración") debería devolver {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter in "abcdefghijklmnopqrstuvwxyz":
      #
      if letter not in result:
        result[letter] = 1
      # Add or increment the value in the dictionary
      else:
        result[letter] += 1
  return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

#Pregunta 8
# ¿Qué devuelven los siguientes comandos cuando animal = "Hippopotamus"?
animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])
#pop, t, us

#Pregunta 9 
# ¿Qué contiene la lista de "colores" después de ejecutar estos comandos?
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)
#['red', 'white', 'yellow', 'blue']

#Pregunta 10
# ¿Qué devuelven los siguientes comandos?
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())
# ['router', 'localhost', 'google'] 