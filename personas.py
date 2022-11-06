##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre, velocidad):
        super().__init__(nombre)
        self.tiempo_entrega = randint(20, 30)
        self.energia = randint(75, 100)
        self.velocidad = velocidad
        

    def repartir(self, pedido):
        if len(pedido) <=2:
            self.energia -= 5
            self.tiempo_entrega = self.tiempo_entrega*1.25
        else:
            self.energia -= 15
            self.tiempo_entrega = self.tiempo_entrega*0.85
        
        
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre):
        super().__init__(nombre) 
        self.habilidad = randint(1,10)
        self.energia = randint(50,80)
        

    def Cocinar(self, informacion_plato):
        for info_plato in informacion_plato.values():
            if info_plato[1] == "Bebestible":
                self.energia -= 10
                return self.energia
            else:
                self.energia -= 15
                return self.energia
        

### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre, platos_preferidos):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos

    def Recibir_pedido(self, pedido, demora):
        pass
### FIN PARTE 2.4 ###


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian")
        un_repartidor = Repartidor("Tomás", 8)
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        

        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad} y parte con una energia de {un_cocinero.energia}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")

        prueba_energia = un_cocinero.Cocinar(PLATOS_PRUEBA)
        print(prueba_energia)

    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
