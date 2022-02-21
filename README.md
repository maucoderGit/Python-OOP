# Platzi OOP Course.

Objetivos para el curso: 
- 
- Entender cómo funciona la **P**rogramación **O**rientada a **O**bjetos.
- Entender cómo medir la eficiencia temporal y espacial de nuestros algoritmos.
- Entender cómo y por qué graficar.
- Aprender a resolver problemas de búsqueda, ordenación y optimización

## POO

¿Qué es una Clase?`

- Una clase, llamandolo de manera simple es un molde, el cual contiene la información básica que debe tener un objeto/Instancia, como sus atributos y métodos, siendo datos básicos que deben contener pero que, en la mayoria de los casos no son iguales a los de otras instancias.

¿Qué es una instancia?

- Cuando hablamos de instancias, nos referimos al objeto que se genera utilizando clases. Imaginemos las clases como un formulario, debes rellenar esa información para poder generar este objeto. Cada copia puede tener datos distintos, al igual que cada objeto entre sí(aunque pertenezcan a la misma clase).

Para definir una clase, simplemente utilizamos el *keyword*

```py
    class
    
    # Example

    class Hotel:
        pass
```

Una vez que tenemos una clase llamada, podemos generar una instacncia llamando al constructor de la clase.

```py
    hotel = Hotel()
```

### Atributos de instancia.

Cabe resaltar, que todas las clases y objetos tienen atributos. Así que utilizaremos el método especial
```py
__init__
```
para definir el estado inicial de nuestra instancia. Recibira como parametro obligatorio
```py
self
```
(Que es simplemente una referencia a la instancia).
```python
class Hotel:

    def __init__(self, max_huespedes, parking):
        self.max_huespedes = max_huespedes
        self.parking = parking
        self.huespedes = 0

hotel = Hotel(50, 20)
print(hotel.parking) # 20
```

### Métodos de instancia:

A diferencia de los atributos, que son quienes se encargan de describir dicho objeto en nuestro programa, los métodos, es el uso y que nos permite hacer con dichas instancias.

De manera más simple, los métodos son las funciones de dicha clase, pero recibe como primer argumento la palabra reservada: 

```py
self
```

```py
class Hotel:

    ```
    def add_coustomer(self, coustomer_recived):
        self.coustomer = coustomer_recived
    
    def checkout(self, coustomer_recived):
        self.coustomer = coustomer_recived
    
    def total_ocupated(self):
        return self.coustomer

    hotel = Hotel(50, 20)
    hotel.add_coustomer(3)
    hotel.checkout(1)
    hotel.total_ocupated() # 2
```   

### Abstract Datatype and Class, Instances:

1. Abstract Datatype: en programación conocemos a estos tipos de datos que tu creas cómo tipo de "Dato Abstracto".

- Como ya sabes de cursos pasados, todo dentro de Python es un objeto, y tiene un tipo.
    - Representación de datos y maneras de interactuar con ellos.

- Tenemos tres formas de interactuar con un objeto:
    - Creación.
    - Manipulación.
    - Destrucción.

- Ventajas:
    - Decomposición.
    - Abstracción, recordemos que abstraer se refiere a usar código que no necesariamente debemos entender como funciona en sí, sino que solo requerimos los resúltados.
    - Encapsulación.

```py
# Definición de una clase

class <Class_Name>(<Super_Class>)
    # Create constructor method
    def __init__(self, <params>):
        <expretion>

    def <method_name>(self, <params>):
        <expretion>
        
```

```py
# Def

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greatings(self, other_person):
        return f'Hola {other_person.name}, me llamo {self.name}'

# use

david = Person("David", 16)
erika = Person("Erika", 24)

david.greatigns(erika) # Hola Erika me llamo David
```

Como puedes ver, las clases nos sirven cómo un tipo de molde el cual rellenaremos con datos, que en este caso son el nombre y la edad de las personas.

2. Instancies: A los objetos, los conocemos como instancias.

- Mientras que la clase es un molde, a los objetos creados les conocemos como instancias.
    - Podemos tener instancias diferentes pero el molde(nuestra clase), seguira siendo el mismo.

- Cuando se crea una instancia, se ejecuta el método __init__.

- Todos los métos de una clase reciben implícitamente como primer parámetro "self".

- Los atributos de clase nos permiten:
    - Representar los datos.
    - Procedimientos para interactuar con los mismos.
    - Mecanismos para esconder la representación interna. La **convención** dentro de Python dice que, para declarar una variable como privada debe empezar con un underscore y luego el nombre del método o de la variable.

```py
    class Coordenada:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distance(self, otra_coordenada):
            x_diff = (self.x - otra_cordenada.x)**2
            y_diff = (self.y - otra_cordenada.y)**2

            return(x_diff + y_diff) ** 0.5

if __name__ == "__main__":
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distance(coord_2))
    print(isintance(coord_2, Coordenada))
```

### Decomposición

Es partir un problema en problemas más pequeños, a esto le llamamos decomponer.

Una computadora es  un buen ejemplo, ya que esta formado de muchísimas piezas, que en conjunto la hacen funcionar.

- Las clases nos permite crear mayores abstracciones en forma de componentes.
- Cada clase se encarge de una parte del problema y el programa se vuelve más fácil de mantener.

Evitando códigos de muchas líneas de código, los cuales suelen tener gran dificultad para entenderlos. Y además estos componentes trabajaran en conjunto para que nuestro programa funcione.

Como podemos ver en el archivo "Descomposicion.py", nuestro código realmente no tiene ningún uso. También notaras que nuestro código se divide en más de una clase, que juntas permiten existir a nuestro automovil.

Además del motor(que es la única clase existente por momento), nuestro automóvil podría contener una clase Asientos, entre muchas otras que conformen al auto pero no esten estríctamente relacionadas.

### Abstracción: 

Es enfocarse en la información relevante.

- Separar información central de detalles secundarios.
- Podemos utilizar variables y métodos(privados y públicos).

Para traer este concepto a la programación, debemos generar una **interfaz**, con la cual interactuaremos directamente con las clases.

Veamos como podemos esconder algunas implementaciones, y como exponer métodos que nos permiten interactuar directamente con nuestras clases.

### Funciones decoradas.

Las funciones decoradas son funciones a las que les añadimos funcionalidades adicionales sin afectar a la función original.

Para eso necesitamos una función de orden superior y entender que son los objetos de primera clase. Conceptos que aprendímos en el curso de Pensamiento computacional con Python.

Para crear una función decorada necesitas una función A, la cual decorará a una función B que le daremos como argumento, y retornaremos una función C, que sera la función B ya decorada.


```py
def funcion_decoradora(funcion):

def wrapper():
    print("Este es el último mensaje...")
    funcion()
    print("Este es el primer mensaje ;)")
return wrapper

def dormir():
	print("*empieza a ver una piece*")

dormir = funcion_decoradora(dormir) 

>>> "Este es el último mensaje..."
>>> "Empiezo a ver One piece"
>>> "Este es el primer mensaje"
```

A esto se le conoce en programación como metaprogramación(*metaprogramming*), porque una parte del programa trata de modifcar otra durante el tiempo de ejecución.

#### Esto parece complejo...

Y si, es una sintaxis poco pythonica, además de ser algo compleja, pero afortunadamente Python tiene en cuenta este problema y podemos usar los decoradores con el simbolo @.

```
    @funcion_decoradora
    def dormir():
        print("Empiezo a ver One Piece")
```

### ¿Y los *getters* y *setters*?

Los getters and setters, en otros lenguajes de programación son utilizados para obtener el valor de un atributo(getters) y también de fijar un valor en el(setters).

En Python, a diferencia del resto(siempre nuestro Python destacando), no podemos generar realmente variables privadas. Si, aunque las declaremos con guión bajo(_) al principio, se sigué podiendo acceder a ellas.

En Python los getters and setters tienen el objetivo de asegurar el encapsulamiento(encargarse de que los datos de un objeto solo puedan cambiarse y definirse mediante los métodos que posee el mismo objeto.) de datos.

```py
    # Código del maestro David Aroesti.

    class User:

        def __init__(self, username, _password):
            self.username = username
            self._password = password

    # Creamos el objeto

    user = User("Mau", "MiContraseñaEsSeguraOjalaNoLaRobenPorUnErrorDeCodigo")
    
    print(user.username, user._password) 
    
    >>> ("Mau", "MiContraseñaEsSeguraOjalaNoLaRobenPorUnErrorDeCodigo")
```

Este es un ejemplo del código sin usar Getters and Setters. Puedes ver que a pesar de declarar esta variable como privada igualmente podemos acceder a alla.

#### Función @property

Es una built-in de Python, crea y retorna propiedades de un objeto. La propiedad de un objeto posee los métodos getter(), setter() y del().

En tanto la función tiene cuatro atributos: property(fget, fset, fdel, fdoc) :

- fget : trae el valor de un atributo.
- fset : define el valor de un atributo.
- fdel : elimina el valor de un atributo.
- fdoc : crea un docstring por atributo.

Veamos un ejemplo del mismo caso implementando la función property():

```py
        class User:

        def __init__(self):
            self.__password = password

        def get_password(self):
            return self.__password

        def set_password(self, password):
            if len(password) < 8:
                raise ValueError("Tu contraseña debe tener al menos 8 caracteres.")
            self.__password = password
        
        def del_password(self):
            del password

        password = property(get_password, set_password, del_password)
```

Ahora creemos el objeto:

```py
usuario = User()

usuario.__password = str(input("Ingresa una contraseña: "))

>>> MiContraseñaMuySeguraYBonita

print(usuario.__password) # Devuelve un error de sintaxis
```

#### ¿Y hay algún decorador que haga esto por nosotros?

¡Pues por supuesto que lo hay! El Decorador @property es uno de muchos en Python, este facilita el uso de getters and setters dentro de nuestro código.

Pero veamos esto en código: 

```py
class User:

    def __init__(self):
        self.__password = password

    @property
    def password(self):
        return self.__password

    # usando el decorador @property
    
    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError("Tu contraseña debe tener al menos 8 caracteres.")
        self.__password = password
```

Y como seguro ya has entendido, el resultado será el mismo que en el anterior.

```py
usuario.password = "MiContraseñaEsMuySegura"
```

### El encapsulamiento en la programación defensiva:

Ya hemos hablado de encapsulamiento aquí, y ya entendímos que debemos establecer métodos para que los atributos de nuestros objetos no sean accecibles ante cualquier desarrollador malintencionado que quiera romper nuestra lógica o un usuario descuidado que se equivoco en la asignación de datos.

**La programación defensiva** va de esto, preveer cada posible situación para que nuestro código no colapse, o en caso de que suceda lo haga con estilo.

Python como bien sabemos es un lenguaje dinámico, en el que no existe un tipado exigente, pero esto tiene consecuencias en la seguridad de nuestros datos y en la lógica de nuestra aplicación.

Los decoradores suelen ser una gran ayuda, porque en caso de que queramos optimizar un código no debemos recaer en la repetición de código, y ayudan a reutilizar lo ya escrito.

### La herencia:

Ya casí estamos tocando fondo en cuanto a POO con Python se trata, pero aún nos quedan dos puntos que tratar. Y uno de ellos es la herencia.

Para entender esto debemos entender que es una superclase y una subclase.

Una superclase es una clase que tiene atributos y métodos que otras clases que reciben estos mismos atributos de ella, evitando repetición de código.
Y las subclases son clases que reciben atributos y/o métodos de una clase superior.

```py
class soda:

    def __init__(self, nombre, sabor):
        self.nombre = nombre
        self.sabor = sabor

    def sonido_de_soda(self):
        print(f'pffffffsss')

class Coka_Cola(soda):

    def __init__(self, nombre, sabor):
        super().__init__(nombre, sabor)

class Pepso(soda):

    def __init__(self, nombre, sabor):
        super().__init__(nombre, sabor)
```

Este es un ejemplo de herencia, y podemos verlo más clar de lo que hablamos.
La clase soda inicializa los atributos y métodos. En cambio la clase Coka_Cola y Pepso, no necesitan hacer esto de nuevo, solo llaman a la función built-in para declarar y luego inicializar dichos atributos.

También puedes ver que al poner el nombre de nuestras nuevas subclases, también encerramos entre parentesis a soda. Esto se debe leer: class a extends b, o en nuestro caso: class Coka_Cola extends soda.

En este caso como heredamos los datos pero no modifican nada se puede escribir en menos líneas de código.

```py
class Coka_Cola(soda):
    pass

class Pepso(soda):
    pass
```

#### Herencia Múltiple:

Las clases pueden heredar mas de una clase, y se aplica el mismo procedimiento que mostramos antes, solo que añadiremos más de una clase.

### Polimorfismo:

Imagina esto, tienes una Clase Animal y en ella guardas el método hablar().

```py
class Animal()

    def __init__(self):
        pass

    def hablar(self)
        print(f'Soy un animal.')
```

Y tienes subclases como lo son perro y gato:

```py
class Perro(Animal):

    def hablar(self):
        print(f'guau guau')

class Gato(Animal):

    def hablar(self):
        print(f'miau miau')
```

Como puedes ver, ambas clases poseen el mismo método hablar, pero no hacen lo mismo.
De esto se trata el polimorfismo, implica que si en una porción de código se invoca un determinado método de un objeto, podrán obtenerse distintos resultados según la clase del objeto.

Como viste en el ejemplo de arriba, puede parecer poco útil, pero una idea que me viene a la mente es con figuras geométricas, y que podamos calcular el diametro o la altura sin poner mucho ojo a cual sea.