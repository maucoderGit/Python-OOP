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
# Definición de una ckase

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