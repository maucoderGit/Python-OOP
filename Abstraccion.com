class Laundry:
    
    def __init__(self):
        pass

    def lavar(self, temperatura="fría"):
        self._llenar_tanque_de_agua(temperatura)
        self._add_soap()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque de agua {temperatura}.')

    def _add_soap(self):
        print("Añadiendo jabon.")

    def _lavar(self):
        print("Lavando ropa.")

    def _centrifugar(self):
        print(f'Centrifugando la ropa.')

if __name__ == "__main__":
    lavadora = Laundry()
    lavadora.lavar()