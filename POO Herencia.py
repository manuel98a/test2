class Vehiculo():

	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enMarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca)
		print("Modelo: ", self.modelo)
		print("En marcha: ", self.enMarcha)
		print("Acelera: ", self.acelera)
		print("Frena: ", self.frena)

class Furgoneta(Vehiculo):

	def carga(self,cargar):
		self.cargado=cargar

		if(self.cargado):
			return "La furgoneta esta cargada."
		else:
			return "La furgoneta no esta cargada."

class Moto(Vehiculo): #hereda de vehiculo
	caballito=""

	def hacerCaballito(self):
		self.caballito="Haciendo caballito" 

	def estado(self): #sobreescribe el metodo padre
		print("Marca: ", self.marca)
		print("Modelo: ", self.modelo)
		print("En marcha: ", self.enMarcha)
		print("Acelera: ", self.acelera)
		print("Frena: ", self.frena)
		print("Caballito: ", self.caballito)

class VehiculoElectrico():

	def __init__(self, marca, modelo):
		super().__init__(marca,modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True

#a la hora de herencia multiple se le da prioridad al primero
class BicicletaElectrica(Vehiculo, VehiculoElectrico):
	pass



#############################################################
############################TEST#############################
#############################################################

moto1=Moto("Honda", "CRB")

moto1.hacerCaballito()

moto1.estado()

print()

furgoneta1=Furgoneta("Nissan", "xr3")

furgoneta1.arrancar()

furgoneta1.estado()

print(furgoneta1.carga(True))

bici1=BicicletaElectrica("Bicita", "Jeje")

print()

bici1.estado()