class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')


def run():
    casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
    print(casilla.region)
    casilla.region = 'Mexico'
    print(casilla.region)

if __name__ == "__main__":
    run()