class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("I'm walking")


# Se lee de esta manera: 
# "La clase ciclista extiende persona"
# Class a extends b
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("I'm moving on my bike")

def run():
    person = Persona("Mau")
    person.avanza()

    ciclista = Ciclista("Juancho")
    ciclista.avanza()


if __name__ == "__main__":
    run()