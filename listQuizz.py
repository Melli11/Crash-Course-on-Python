# Pregunta 1 
# Dada una lista de nombres de archivo, queremos cambiar el nombre de todos los archivos con extensión hpp a la extensión h.
# Para hacer esto, nos gustaría generar una nueva lista llamada newfilenames, que consta de los nuevos nombres de archivo. 
# Complete los espacios en blanco en el código utilizando cualquiera de los métodos que ha aprendido hasta ahora, 
# como un bucle for o una lista de comprensión.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
def checkExtensionWord(word):
    if (".hp" in word):
        return True
    else:
        return False

def modificarPalabraConExtension(word):
    word = word [:word.index(".hp")+2]
    return word

# palabraPrueba = "picapiedra.hpp"
# print (modificarPalabraConExtension(palabraPrueba))
newfilenames = []
for index,word in enumerate (filenames):
    if(checkExtensionWord(word) == True): #".hp"
        newfilenames.append(modificarPalabraConExtension(word))
    else:
        newfilenames.append(filenames[index])
    
print(newfilenames) 


# Pregunta 2 
# Vamos a crear una función que convierta el texto en pig latin:
# una transformación de texto simple que modifica cada palabra moviendo el primer carácter al final y agregando "ay" al final.
# Por ejemplo, python termina como ythonpay

def convertirAPigLatin(word,primerCaracter,say):
  word = word[1:] + primerCaracter + say  
  return word

def pig_latin(text):
  words = text.split()
  # primerCaracter = word[index][0]
  say = "ay"
  newList = []
  # for index in words:
  for index,word in enumerate (words):
    newList.append(convertirAPigLatin(word,word[0],say))
  return " " .join (newList)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# Pregunta 3
# Los permisos de un archivo en un sistema Linux se dividen en tres conjuntos de tres permisos: lectura, escritura y ejecución para el propietario, el grupo y otros.
# Cada uno de los tres valores se puede expresar como un número octal que suma cada permiso, 
# con 4 correspondientes a lectura, 2 a escritura y 1 a ejecución. O se puede escribir con una cadena usando las letras r, w y x o - cuando no se otorga el permiso.
# Por ejemplo: 640 es lectura/escritura para el propietario, lectura para el grupo y sin permisos para los demás; convertido a una cadena, 
# sería: "rw-r-----" 755 es lectura/escritura/ejecución para el propietario, y lectura/ejecución para el grupo y otros; convertido a una cadena, 
# sería: "rwxr-xr-x" Complete los espacios en blanco para que el código convierta un permiso en formato octal en un formato de cadena.

# Pregunta 4 
# Tuples and lists are very similar types of sequences. What is the main thing that makes a tuple different from a list?

# Pregunta 5
# Pregunta 5 La función group_list acepta un nombre de grupo y una lista de miembros, y devuelve una cadena con el formato: group_name: miembro1, miembro2, …
# Por ejemplo, group_list("g", ["a","b","c"] ) devuelve "g: a, b, c". Complete los espacios en esta función para hacer eso.

prueba1 = "algo"
prueba2 = 'mas'
resultado = prueba1 + prueba2
print (resultado) # imprime "algomas"

def group_list(group, users):
  dosPuntos = ": "
  group = group + dosPuntos
  result = ", ".join (users)
  return group+result



# Pregunta 6
# La función guest_list lee una lista de tuplas con el nombre, la edad y la profesión de cada invitado a la fiesta, e imprime la oración
# "El invitado tiene X años y trabaja como __". para cada uno. Por ejemplo, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer"))
# debe imprimirse: Ken tiene 30 años y trabaja como Chef. 
# Pat tiene 35 años y trabaja como abogado. Amanda tiene 25 años y trabaja como Ingeniera. Complete los espacios en esta función para hacer eso.