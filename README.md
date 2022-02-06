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