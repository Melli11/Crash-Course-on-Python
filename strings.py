# Modify the double_word function so that it returns the same word repeated twice,
# followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.

# Modifique la función double_word para que devuelva la misma palabra repetida dos veces,
#  seguida de la longitud de la nueva palabra duplicada. Por ejemplo, palabra_doble("hola") debería devolver hellohola10.

def double_word(word):
    aux = word*2 + str (2*len(word)) 
    return aux

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

# Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True
#  if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

# ¿Quieres intentarlo tú mismo? ¡Sé mi invitado! Modifique la función first_and_last para que devuelva True 
# si la primera letra de la cadena es la misma que la última letra de la cadena, False si son diferentes. Recuerda que puedes acceder a los caracteres usando mensaje[0] o mensaje[-1]. 
# Tenga cuidado con la forma en que maneja la cadena vacía, que debería devolver True ya que nada es igual a nada

def first_and_last(message):
    if message == "":
        return True
    if message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))