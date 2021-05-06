#Emilio Campuzano Mejia A01378948
#Lorena Palomino Castillo A01378477
"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    import turtle
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    turtle.circle(end.x - start.y)
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
"Se presiona la tecla u para poder rehacer alguna acción ya hecha"
onkey(undo, 'u')
"Se presiona la tecla K para cambiar a color negro"
onkey(lambda: color('black'), 'K')
"Se presiona la tecla W para cambiar a color blanco"
onkey(lambda: color('white'), 'W')
"Se presiona la tecla G para cambiar a color verde"
onkey(lambda: color('green'), 'G')
"Se presiona la tecla B para cambiar a color azul"
onkey(lambda: color('blue'), 'B')
"Se presiona la tecla R para cambiar a color rojo"
onkey(lambda: color('red'), 'R')
"Se presiona la tecla Y para cambiar a color amarillo"
onkey(lambda: color('yellow'), 'Y')
"Se presiona la tecla l para cambiar la figura a una linea"
onkey(lambda: store('shape', line), 'l')
"Se presiona la tecla s para cambiar la figura a una cuadrado"
onkey(lambda: store('shape', square), 's')
"Se presiona la tecla c para cambiar la figura a una circulo"
onkey(lambda: store('shape', circle), 'c')
"Se presiona la tecla r para cambiar la figura a una rectangulo"
onkey(lambda: store('shape', rectangle), 'r')
"Se presiona la tecla t para cambiar la figura a una triangulo"
onkey(lambda: store('shape', triangle), 't')

done()
