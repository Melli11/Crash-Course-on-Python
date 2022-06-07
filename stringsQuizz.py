# 1. Pregunta 1
# La función is_palindrome comprueba si una cadena es un palíndromo.
# Un palíndromo es una cadena que se puede leer igualmente de izquierda a derecha o de derecha a izquierda, 
# omitiendo los espacios en blanco e ignorando las mayúsculas.
# Ejemplos de palíndromos son palabras como kayak y radar, y frases como "Never Odd or Even". 

# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = ""
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for ___:
# 		# Add any non-blank letters to the 
# 		# end of one string, and to the front
# 		# of the other string. 
# 		if ___:
# 			new_string = ___
# 			reverse_string = ___
# 	# Compare the strings
# 	if ___:
# 		return True
# 	return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

#Pregunta 2
#Usando el método de formato, complete los espacios en la función convert_distance para que devuelva la frase "X millas es igual a Y km",
#  con Y con solo 1 lugar decimal. Por ejemplo, convert_distance(12) debería devolver "12 millas equivalen a 19,2 km".

def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

#Pregunta 3
# Si tenemos una variable de cadena llamada Weather = "Rainfall", ¿cuál de las siguientes imprimirá la subcadena o todos los caracteres antes de la "f"?
Weather = "Rainfall"
# print(weather[:"f"])

print(Weather[:4]) #ok
print(Weather[4:])
print(Weather[1:4])
# print(Weather[:"f"]) error

# Pregunta 4
# Complete los espacios en blanco en la función nametag para que use el método de formato para devolver first_name 
# y la primera inicial de last_name seguido de un punto. Por ejemplo, nametag("Jane", "Smith") debería devolver "Jane S".
def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G."


# Pregunta 5
# La función replace_ending reemplaza la cadena anterior en una oración con la nueva cadena, pero solo si la oración termina con la cadena anterior.
# Si hay más de una ocurrencia de la cadena anterior en la oración, solo se reemplaza la que está al final, no todas.
# Por ejemplo, replace_ending("abcabc", "abc", "xyz") debería devolver abcxyz, no xyzxyz o xyzabc.
# La comparación de cadenas distingue entre mayúsculas y minúsculas, por lo que replace_ending("abcabc", "ABC", "xyz") debería devolver abcabc (sin cambios).

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence
	#Compruebe si la cadena anterior está al final de la oración
	if  sentence.count(old)>=2:
		i = len(old)
		new_sentence = sentence[:-i]+ new
		return new_sentence
	if  sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		# Usando i como el índice de corte, combine la parte
		# de la oración hasta la cadena coincidente en el
		# final de la nueva cadena
		i = sentence.index(old)
		# new_sentence = sentence[:i]+ new
		new_sentence = sentence[:i]+ new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"