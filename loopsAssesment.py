# Pregunta 1
# Fill in the blanks of this code to print out the numbers 1 through 7.

number = 1
while number <= 7:
	print(number, end= " ")
	number = number +1

# Pregunta 2
# La función show_letters debe imprimir cada letra de una palabra en una línea separada. Complete los espacios en blanco para que eso suceda.

def show_letters(word):
	for x in word:
		print(str(x),end = "\n")

show_letters("Hello")
# Should print one line per letter

#Pregunta 3

# Completa la función dígitos(n) que devuelve cuántos dígitos tiene el número. 
# Por ejemplo: 25 tiene 2 dígitos y 144 tiene 3 dígitos. Consejo: puedes averiguar los dígitos de un número dividiéndolo por 10 una vez por dígito 
#  hasta que no queden dígitos.