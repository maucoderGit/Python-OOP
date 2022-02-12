class Automovil:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = "rest"
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo="slowly"):
        if tipo == "fast":
            self._motor.inyecta_gasolina(10)
        else:
            self._status = "moving"

class Motor:

    def __init__(self, cilindros, tipo="Gas"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temp = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Seats:

    def __init__(self, material, tipo):
        self.material = material
        self.tipo = tipo

    def reclinar(self):
        pass