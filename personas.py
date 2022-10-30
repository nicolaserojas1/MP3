##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona():
    def __init__(self, nombre_persona):
        self.nombre = nombre_persona
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre_persona, energia, velocidad):
        super().__init__(nombre_persona)
        self.energia = energia
        self.velocidad = velocidad

    def repartir(self, pedido, distancia):
        pass
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre_persona, energia, habilidad):
        super().__init__(nombre_persona) 
        self.energia = energia
        self.habilidad = habilidad

    def Cocinar(self, solicitar):
        pass
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre_persona, exigencia, distancia, plato_preferido):
        super().__init__(nombre_persona)
        self. exigencia = exigencia
        self. distancia = distancia
        self.plato_preferido = plato_preferido

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
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
