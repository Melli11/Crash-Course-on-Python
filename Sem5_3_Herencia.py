
# Vamos a crear una nueva clase juntos y heredar de ella. A continuación tenemos una clase base llamada Ropa.
# Juntos, creemos una segunda clase, llamada Shirt, que hereda métodos de la clase Clothing. Complete los espacios en blanco para que funcione correctamente.

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()


# ---------------------------------------------------------------------------------------------------------------------

# Ampliemos un poco nuestras clases de ropa de la pregunta anterior en el video.
#  Tu misión: terminar el método "Stock_by_Material" e iterar sobre la cantidad de cada artículo de un material dado que está en stock.
#  Cuando haya terminado, el guión debe agregar hasta 10 polos de algodón.

class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)




# ---------------------------------------------------------------------------------------------------------------------
#Digamos que queremos usar el módulo de aprendizaje profundo de Keras. Al ejecutar el script, se imprime un error que indica que no se 
# pudo encontrar el módulo Keras. ¿Qué nos podríamos haber perdido?

# RTA: We need to import the Keras module