
import turtle
import math

### A library of functions that draw fractals.
### @author Peter Sujan


### Various utility methods, including wrappers around turtle methods.

def reset():
    turtle.reset()

def drawSquare(size, fill):
    turtle.fill(fill)
    for i in range(4):
        turtle.fd(size)
        turtle.right(90)
    turtle.fill(False)

def drawTriangle(size, fill):
    turtle.fill(fill)
    for i in range(3):
        turtle.fd(size)
        turtle.right(120)
    turtle.fill(False)


### Functions that draw fractals.


def koch(size, level):
    """ One side of the Koch Snowflake.
    http://en.wikipedia.org/wiki/Koch_snowflake
    """
    
    if level < 1:
        turtle.fd(size)
    else:
        koch(size / 3.0, level - 1)
        turtle.left(60)
        koch(size / 3.0, level - 1)
        turtle.right(120)
        koch(size / 3.0, level - 1)
        turtle.left(60)
        koch(size / 3.0, level - 1)


def fullKoch(size, level):
    """ The full Koch Snowflake.
    http://en.wikipedia.org/wiki/Koch_snowflake
    """

    for i in range(3):
        koch(size, level)
        turtle.right(120)


def cCurve(size, level):
    """ The Levy C-Curve fractal.
    http://en.wikipedia.org/wiki/C-curve
    """

    if level < 1:
        turtle.fd(size)
    else:
        turtle.left(45)
        cCurve(size / 2.0, level - 1)
        turtle.right(90)
        cCurve(size / 2.0, level - 1)
        turtle.left(45)

def squiral(size, level):
    """ A square spiral. """

    if level < 1:
        turtle.fd(size)
    else:
        turtle.fd(size * level)
        turtle.right(90)
        squiral(size, level - 1)


def UMCTriangle(size, angle, level):
    """ A 'uniform mass center triangle' fractal """
    newAngle = angle / 2.0
    obtuse = 180 - angle * 2
    if level < 1:
            turtle.fd(size)
            turtle.left(180 - angle + newAngle)
            turtle.fd(size / (2 * math.cos(math.radians(newAngle))))
            turtle.bk(size / (2 * math.cos(math.radians(newAngle))))
            turtle.right(newAngle)
            
            turtle.fd(size / (2 * math.cos(math.radians(angle))))
            turtle.left(180 - obtuse + obtuse / 2.0)
            turtle.fd(size / (2 * math.cos(math.radians(angle))) * math.sin(math.radians(newAngle)) / math.sin(math.radians(180 - newAngle - obtuse / 2.0)))
            turtle.bk(size / (2 * math.cos(math.radians(angle))) * math.sin(math.radians(newAngle)) / math.sin(math.radians(180 - newAngle - obtuse / 2.0)))
            turtle.right(obtuse / 2.0)

            turtle.fd(size / (2 * math.cos(math.radians(angle))))
            turtle.left(180 - angle + newAngle)
            turtle.fd(size / (2 * math.cos(math.radians(newAngle))))
            turtle.bk(size / (2 * math.cos(math.radians(newAngle))))
            turtle.right(newAngle)
            
    else:
        for i in range(3):
            UMCTriangle(size, newAngle, level - 1)
            turtle.fd(size)
            
            turtle.fd(size / (2 * math.cos(math.radians(angle))))

            turtle.fd(size / (2 * math.cos(math.radians(angle))))
            
        

def accidentalButCool(size, angle, level):
    newAngle = angle / 2.0
    obtuse = 180 - angle
    if level < 1:
        for i in range(3):
            turtle.fd(size)
            turtle.left(obtuse)
            turtle.fd(size / (2 * math.cos(math.radians(newAngle))))
            turtle.bk(size / (2 * math.cos(math.radians(newAngle))))
            turtle.right(newAngle)
    else:
        for i in range(3):
            accidentalButCool(size, newAngle, level - 1)



def gosperBad(size, level):
    for i in range(6):
        gosperBadHelper(size, level)
        turtle.right(60)


def gosperBadHelper(size, level):
    if level < 1:
        turtle.fd(size)
    else:
        turtle.up()
        turtle.right(90)
        turtle.fd(size / math.sqrt(9))
        turtle.left(90)
        turtle.fd(size / 6.0)
        turtle.left(60)
        turtle.down()
        gosperHelper(size / 3.0, level - 1)
        turtle.right(60)
        gosperHelper(size / 3.0, level - 1)
        turtle.right(60)
        gosperHelper(size / 3.0, level - 1)
        turtle.up()
        turtle.left(60)
        turtle.fd(size / 6.0)
        turtle.left(90)
        turtle.fd(size / math.sqrt(9))
        turtle.right(90)


def gosper(size, level, direction):
    """ The Gosper Curve.
    http://en.wikipedia.org/wiki/Gosper_curve
    """

    if level < 1:
        if direction > 0:
            turtle.right(60)
            turtle.fd(size)
            turtle.left(60)
            turtle.fd(2 * size)
            turtle.left(120)
            turtle.fd(size)
            turtle.left(60)
            turtle.fd(size)
            turtle.right(120)
            turtle.fd(size)
            turtle.right(60)
            turtle.fd(size)
        else:
            turtle.fd(size)
            turtle.left(60)
            turtle.fd(size)
            turtle.left(120)
            turtle.fd(size)
            turtle.right(60)
            turtle.fd(size)
            turtle.right(120)
            turtle.fd(2 * size)
            turtle.right(60)
            turtle.fd(size)
            turtle.left(60)
    else:
        if direction > 0:
            turtle.right(60)
            gosper(size / 2.5, level - 1, -1)
            turtle.left(60)
            gosper(size / 2.5, level - 1, 1)
            gosper(size / 2.5, level - 1, 1)
            turtle.left(120)
            gosper(size / 2.5, level - 1, 1)
            turtle.left(60)
            gosper(size / 2.5, level - 1, -1)
            turtle.right(120)
            gosper(size / 2.5, level - 1, -1)
            turtle.right(60)
            gosper(size / 2.5, level - 1, 1)
        else:
            gosper(size / 2.5, level - 1, -1)
            turtle.left(60)
            gosper(size / 2.5, level - 1, 1)
            turtle.left(120)
            gosper(size / 2.5, level - 1, 1)
            turtle.right(60)
            gosper(size / 2.5, level - 1, -1)
            turtle.right(120)
            gosper(size / 2.5, level - 1, -1)
            gosper(size / 2.5, level - 1, -1)
            turtle.right(60)
            gosper(size / 2.5, level - 1, 1)
            turtle.left(60)


def vicsekS(size, level):
    """ The saltire form of the Vicsek fractal. """
    newSize = size / 3.0
    if level < 1:
        turtle.down()
        drawSquare(newSize, True)
        turtle.up()
        turtle.fd(2 * newSize)
        turtle.down()
        drawSquare(newSize, True)
        turtle.up()
        turtle.bk(2 * newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.left(90)
        turtle.fd(newSize)
        turtle.down()
        drawSquare(newSize, True)
        turtle.up()
        turtle.bk(newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.left(90)
        turtle.down()
        drawSquare(newSize, True)
        turtle.up()
        turtle.fd(2 * newSize)
        turtle.down()
        drawSquare(newSize, True)
        turtle.up()
        turtle.bk(2 * newSize)
        turtle.left(90)
        turtle.fd(2 * newSize)
        turtle.right(90)

    else:
        turtle.down()
        vicsekS(newSize, level - 1)
        turtle.up()
        turtle.fd(2 * newSize)
        turtle.down()
        vicsekS(newSize, level - 1)
        turtle.up()
        turtle.bk(2 * newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.left(90)
        turtle.fd(newSize)
        turtle.down()
        vicsekS(newSize, level - 1)
        turtle.up()
        turtle.bk(newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.left(90)
        turtle.down()
        vicsekS(newSize, level - 1)
        turtle.up()
        turtle.fd(2 * newSize)
        turtle.down()
        vicsekS(newSize, level - 1)
        turtle.up()
        turtle.bk(2 * newSize)
        turtle.left(90)
        turtle.fd(2 * newSize)
        turtle.right(90)
        

def vicsekC(size, level):
    """ The cross form of the Vicsek fractal. """
    newSize = size / 3.0
    if level < 1:
        turtle.up()
        turtle.fd(newSize)
        turtle.down()
        drawSquare(newSize, True)
        turtle.up()
        turtle.bk(newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.left(90)
        turtle.down()
        drawSquare(newSize, True)
        turtle.fd(newSize)
        drawSquare(newSize, True)
        turtle.fd(newSize)
        drawSquare(newSize, True)
        turtle.bk(newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.left(90)
        drawSquare(newSize, True)
        turtle.up()
        turtle.left(90)
        turtle.fd(2 * newSize)
        turtle.right(90)
        turtle.bk(newSize)
        

    else:
        turtle.up()
        turtle.fd(newSize)
        turtle.down()
        vicsekC(newSize, level - 1)
        turtle.up()
        turtle.bk(newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.left(90)
        turtle.down()
        vicsekC(newSize, level - 1)
        turtle.fd(newSize)
        vicsekC(newSize, level - 1)
        turtle.fd(newSize)
        vicsekC(newSize, level - 1)
        turtle.bk(newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.left(90)
        vicsekC(newSize, level - 1)
        turtle.up()
        turtle.left(90)
        turtle.fd(2 * newSize)
        turtle.right(90)
        turtle.bk(newSize)




def dragon(size, level, direction):
    """ The Dragon Curve.
    http://en.wikipedia.org/wiki/Dragon_curve
    """

    if level < 1:
        turtle.down()
        turtle.right(direction * 45)
        turtle.fd(size)
        turtle.left(direction * 90)
        turtle.fd(size)
        turtle.right(direction * 45)
    else:
        turtle.down()
        turtle.right(direction * 45)
        dragon(size / math.sqrt(2), level - 1, 1)
        turtle.left(direction * 90)
        dragon(size / math.sqrt(2), level - 1, -1)
        turtle.right(direction * 45)


def sierpinski(size, level):
    """ The Sierpinski Triangle
    https://en.wikipedia.org/wiki/Sierpinski_triangle
    """

    if level < 1:
        turtle.left(60)
        drawTriangle(size, True)
        turtle.right(60)
    else:
        sierpinski(size / 2.0, level - 1)
        turtle.left(60)
        turtle.fd(size / 2.0)
        turtle.right(60)
        sierpinski(size / 2.0, level - 1)
        turtle.left(60)
        turtle.bk(size / 2.0)
        turtle.right(60)
        turtle.fd(size / 2.0)
        sierpinski(size / 2.0, level - 1)
        turtle.bk(size / 2.0)


def sierpinskiArrowhead(size, level, direction):
    """ The Sierpinski Arrowhead Curve.
    https://en.wikipedia.org/wiki/Sierpi%C5%84ski_arrowhead_curve
    """

    if level < 1:
        turtle.left(60 * direction)
        turtle.fd(size * direction)
        turtle.right(60 * direction)
        turtle.fd(size * direction)
        turtle.right(60 * direction)
        turtle.fd(size * direction)
        turtle.left(60 * direction)
    else:
        turtle.right(120 * direction)
        sierpinskiArrowhead(size / 2.0, level - 1, direction * -1)
        turtle.left(120 * direction)
        sierpinskiArrowhead(size / 2.0, level - 1, direction)
        turtle.left(120 * direction)
        sierpinskiArrowhead(size / 2.0, level - 1, direction * -1)
        turtle.right(120 * direction)


def tSquare(size, level):
    """ The T-Square fractal.
    http://en.wikipedia.org/wiki/T-Square_%28fractal%29
    """

    if level < 1:
        drawSquare(size, True)
    else:
        drawSquare(size, True)
        turtle.bk(size / 4.0)
        turtle.left(90)
        turtle.fd(size / 4.0)
        turtle.right(90)
        tSquare(size / 2.0, level - 1)
        turtle.up()
        turtle.fd(size)
        turtle.down()
        tSquare(size / 2.0, level - 1)
        turtle.right(90)
        turtle.fd(size)
        turtle.left(90)
        tSquare(size / 2.0, level - 1)
        turtle.bk(size)
        tSquare(size / 2.0, level - 1)
        turtle.left(90)
        turtle.up()
        turtle.fd(size * 3 / 4.0)
        turtle.down()
        turtle.right(90)
        turtle.fd(size / 4.0)
        

def pythagoras(size, level):
    """ The Pythagoras Tree fractal.
    http://en.wikipedia.org/wiki/Pythagoras_tree_%28fractal%29
    """

    if level < 1:
        drawSquare(size, True)
    else:
        newSize = size / 2.0 * math.sqrt(2)
        drawSquare(size, True)
        turtle.left(135)
        turtle.fd(newSize)
        turtle.right(90)
        pythagoras(newSize, level - 1)
        turtle.left(90)
        turtle.bk(newSize)
        turtle.right(135)
        turtle.fd(size)
        turtle.left(135)
        turtle.fd(newSize)
        turtle.right(90)
        turtle.fd(newSize)
        turtle.right(90)
        pythagoras(newSize, level - 1)
        turtle.left(90)
        turtle.bk(newSize)
        turtle.left(90)
        turtle.bk(newSize)
        turtle.right(135)
        turtle.bk(size)

