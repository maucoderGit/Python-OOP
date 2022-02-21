class Rectangle:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangle):

    def __init__(self, lado):
        super().__init__(lado, lado)
    
if __name__ == "__main__":
    rectangle = Rectangle(10, 4)
    print(rectangle.area())

    square = Cuadrado(10)
    print(square.area())