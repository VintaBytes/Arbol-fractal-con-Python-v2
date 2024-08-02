# Arbol Fractal en Python (L-System) V2.

Este script utiliza la librería `turtle` en Python para dibujar un árbol fractal. El árbol se genera utilizando un sistema de L (Lindenmayer system), un método de modelado fractal que aplica reglas recursivas para crear formas complejas.

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>
<span><img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"/></span>

## Resultado
<img src="https://github.com/user-attachments/assets/3b66dfad-38f1-4421-9e88-afa9b2c3f18d" width="640px">

## Explicación del Código

### Importaciones
```python
from turtle import *
import time
import random
```
El código importa la librería `turtle` para dibujar gráficos, así como `time` y `random` para funciones de tiempo y generación de números aleatorios.

### Configuración Inicial
```python
speed(10)
rt(-90)
angle = 10
```
- `speed(10)`: Ajusta la velocidad de dibujo del turtle.
- `rt(-90)`: Rota el turtle 90 grados a la izquierda para que empiece a dibujar hacia arriba.
- `angle = 10`: Define el ángulo base de ramificación.

### Función Recursiva `y`
```python
def y(sz, level):
    final_level = level
    if level > 0:
        colormode(255)

        if level < 7:
            if level == 1:
                pensize(6)
            else:
                pensize(level * 1.5)
            largo = 0.8 * (sz + random.randrange(-2, 15))
            colorR = 200 - level * 15
            colorG = 100 + level * 15
            colorB = 47 - level
            angulo = angle + random.randrange(0, int(8 - level) * 3)
        else:
            pensize(level)
            largo = 0.9 * sz + random.randrange(-12, 15)
            colorR = 141 - level * 4
            colorG = 70 - level * 2
            colorB = 47 - level
            angulo = angle + level * random.randrange(0, 15) / 15

        if (random.randrange(1, 100) > (level * 4)) or (level > random.randrange(7, 12)):
            print(level)
            pencolor(colorR, colorG, colorB)
            fd(largo)
            rt(angulo)
            y(largo, level - 1)

            if (random.randrange(1, 100) > 50):
                penup()
            pencolor(colorR, colorG, colorB)
            lt(2 * angulo)
            y(largo, level - 1)
            pendown()

            pencolor(colorR, colorG, colorB)
            rt(angulo)
            fd(-largo)
```
Esta función es recursiva y se llama a sí misma para dibujar ramas del árbol. Los parámetros son:
- `sz`: El tamaño de la rama.
- `level`: El nivel de recursión.

Dentro de la función:
- `colormode(255)`: Ajusta el modo de color.
- `pensize(...)`: Ajusta el grosor del lápiz basado en el nivel.
- `pencolor(...)`: Cambia el color del lápiz.
- `fd(sz)`: Avanza el lápiz para dibujar una rama.
- `rt(angulo)`: Gira el lápiz a la derecha.
- `lt(2 * angulo)`: Gira el lápiz a la izquierda dos veces el ángulo.
- `fd(-sz)`: Retrocede el lápiz para volver a la base de la rama actual.
- `random.randrange(...)`: Introduce aleatoriedad en los tamaños y ángulos de las ramas.

### Configuración de la Pantalla y Llamada Inicial
```python
setup(1024, 800, 0, 0)
penup()
goto(0, -350)
pendown()
time.sleep(8)
y(80, 14)
exitonclick()
```
- `setup(1024, 800, 0, 0)`: Configura el tamaño de la ventana del dibujo.
- `penup()`, `goto(0, -350)`, `pendown()`: Posiciona el turtle en la base del árbol.
- `time.sleep(8)`: Pausa antes de comenzar el dibujo.
- `y(80, 14)`: Llama a la función `y` con un tamaño inicial de 80 y nivel de recursión de 14.
- `exitonclick()`: Espera un clic para cerrar la ventana del dibujo.

---

Con esta explicación, el lector del `README.md` tendrá una comprensión clara de cómo el código genera un árbol fractal utilizando la librería `turtle` y la recursión.
