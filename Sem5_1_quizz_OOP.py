# Pongamos a prueba su conocimiento sobre el uso de la notación de puntos para acceder a métodos y atributos en un objeto.
#  Digamos que tenemos una clase llamada Birds. Las aves tienen dos atributos: color y número.
#  Birds también tiene un método llamado count() que cuenta el número de pájaros (agrega un valor al número).
#  ¿Cuál de las siguientes líneas de código imprimirá correctamente el número de pájaros? ¡Tenga en cuenta que el número de pájaros es 0 hasta que se cuenten!

# OPCION 1

# bluejay.number = 0
# print(bluejay.number)

# OPCION 2

# print(bluejay.number.count())  <--RTA

# OPCION 3

# bluejay.count()
# print(bluejay.number)

# OPCION 4

# print(bluejay.number)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#La creación de nuevas instancias de objetos de clase puede ser una excelente manera de realizar un seguimiento de los valores utilizando atributos asociados con el objeto. 
# Los valores de estos atributos se pueden cambiar fácilmente a nivel de objeto. El siguiente código ilustra una cita famosa de George Bernard Shaw,
#  usando objetos para representar personas. Complete los espacios en blanco para que el código satisfaga el comportamiento descrito en la cita.

# “Si tú tienes una manzana y yo tengo una manzana e intercambiamos estas manzanas entonces
# tú y yo todavía tendremos una manzana cada uno. Pero si tu tienes una idea y yo la tengo
# una idea e intercambiamos estas ideas, entonces cada uno de nosotros tendrá dos ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Aquí, a pesar de que G.B. Cita de Shaw,nuestros personajes han comenzado con diferentes 
# cantidades de manzanas para que podamos observar mejor los resultados.
#Vamos a hacer que Martin y Johanna intercambien TODAS sus manzanas uno con el otro.
#Pista: ¿cómo cambiarías los valores de las variables,
# para que "tú" y "yo" intercambiemos TODAS sus manzanas entre nosotros?
#¿Necesita una variable temporal para almacenar uno de los valores? 
# Es posible que necesite más de una línea de código para hacer eso, lo cual está bien.
    aux_you = you.apples
    aux_me = me.apples
    you.apples = aux_me 
    me.apples = aux_you
    return you.apples, me.apples
    
def exchange_ideas(you, me):
#"tú" y "yo" compartiremos nuestras ideas.
#Qué operaciones deben realizarse, 
# para que cada objeto reciba el número compartido de ideas?
#Pista: ¿cómo asignarías el número total de ideas a cada atributo de la idea?
# ¿Necesita una variable temporal para almacenar la suma de ideas,
#  o puedes encontrar otra manera? 
#Use tantas líneas de código como necesite aquí.
    total_ideas = you.ideas + me.ideas
    you.ideas = total_ideas 
    me.ideas = total_ideas

    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# La clase Ciudad tiene los siguientes atributos: nombre, país (donde se encuentra la ciudad), elevación (medida en metros) y 
# población (aproximada, según estadísticas recientes). Rellene los espacios en blanco de la función max_elevation_city para 
# devolver el nombre de la ciudad y su país (separados por una coma), al comparar las 3 instancias definidas para una población mínima especificada.
# Por ejemplo, llamar a la función para una población mínima de 1 millón: max_elevation_city(1000000) debería devolver "Sofía, Bulgaria".

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):

# Inicializar la variable que contendrá la información de la ciudad con la elevación más alta
	return_city = City()

# Evaluar la 1ra instancia para cumplir con los requisitos:
# la ciudad #1 tiene al menos min_population y ¿Es su elevación la más alta evaluada hasta ahora?
	if city1.population >= min_population and city1.elevation>return_city.elevation:
    
		return_city = city1
# Evaluar la 2da instancia para cumplir con los requisitos:
# la ciudad #2 tiene al menos min_population y ¿Es su elevación la más alta evaluada hasta ahora?
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2
# Evaluar la 3ra instancia para cumplir con los requisitos:
# la ciudad #3 tiene al menos min_population y ¿Es su elevación la más alta evaluada hasta ahora?
	if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3
	#Format the return string
	if return_city.name:
		return  ("{}, {}".format(return_city.name, return_city.country))
	else:
		return ""
print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ¿Qué hace que un objeto sea diferente de una clase?

# RTA: Un objeto es una instancia específica de una clase.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tenemos dos muebles: una mesa de madera marrón y un sofá de cuero rojo.
# Rellene los espacios en blanco después de la creación de cada 
# instancia de clase Furniture, de modo que la función describe_furniture 
# pueda formatear una oración que describa estas piezas de la siguiente manera: 
# "Este mueble está hecho de {color} {material}"

class Furniture: # Furniture = Muebles
	color = ""
	material = ""

table = Furniture() #table = mesa
table.color = "brown"
table.material = "wood" #madera


couch = Furniture() #couch = sofa
couch.color = "red"
couch.material = "leather" #leather = cuero

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"