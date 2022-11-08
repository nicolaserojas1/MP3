##############################################################
from cmath import inf
from random import randint
from platos import Comestible, Bebestible, Plato
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
        self.demora = 0
        

    def repartir(self, pedido):
        if len(pedido) <=2:
            self.energia -= 5
            self.tiempo_entrega = self.tiempo_entrega*1.25
            self.demora = self.tiempo_entrega
            return self.demora
        else:
            self.energia -= 15
            self.tiempo_entrega = self.tiempo_entrega*0.85
            self.demora = self.tiempo_entrega
            return self.demora
        
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre):
        super().__init__(nombre) 
        self.habilidad = randint(1,10)
        self.energia = randint(50,80)
        

    def Cocinar(self, informacion_plato):
        for info_plato in informacion_plato.values():
            if "Bebestible" in info_plato[1]:
                bebestible = Bebestible(info_plato[0])
                bebestible.DificultadPlato() 
                if "Grande" in bebestible.tamano:
                    self.energia -= 10
                elif "Mediano" in bebestible.tamano:
                    self.energia -= 8
                else: 
                    self.energia -= 5
                if bebestible.dificultad > self.habilidad:
                    bebestible.calidad *= 0.7
                    return bebestible
                else:
                    bebestible.calidad *= 1.5
                    return bebestible            
            else:
                comestible = Comestible(info_plato[0])
                self.energia -= 15
                return comestible




### FIN PARTE 2.3 ###                self.DificultadPlato(info_plato[0])


### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre, platos_preferidos):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos
        self.calificacion = 10

    def Recibir_pedido(self, pedido:object):
        if pedido <= self.platos_preferidos or Repartidor.demora >= 2:
            self.calificacion = self.calificacion/2
            for i in pedido:
                if Plato.calidad >= 11:
                    self.calificacion += 1.3
                    return self.calificacion
                elif Plato.calidad <= 8:
                    self.calificacion -=3 
                    return self.calificacion
        else:
            return self.calificacion 




### FIN PARTE 2.4 ###


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural","Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }        
        un_cocinero = Cocinero("Cristian")
        un_repartidor = Repartidor("Tomás", 8)
        un_cliente = Cliente("Alberto", ["Pisco Souer", "Lomo a lo proble"])
        

        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad} y parte con una energia de {un_cocinero.energia}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
        tiempo_Demo = un_repartidor.repartir(PLATOS_PRUEBA)
        print(tiempo_Demo)
        
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
