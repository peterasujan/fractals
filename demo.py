
from fractals import *

t.speed(0)
reset()

raw_input("Press [ENTER] to continue")
print("Koch snowflake")
reset()
fullKoch(300, 3)

raw_input("Press [ENTER] to continue")
print("C-curve")
reset()
cCurve(1800, 8)

raw_input("Press [ENTER] to continue")
print("Gosper curve")
reset()
gosper(100, 2, 1)

raw_input("Press [ENTER] to continue")
print("Vicsek fractal")
reset()
vicsekC(250, 2)

raw_input("Press [ENTER] to continue")
print("Sierpinski triangle")
reset()
sierpinski(300, 3)

raw_input("Press [ENTER] to continue")
print("Hexaflake")
reset()
hexaflake(150, 2, False)

raw_input("Press [ENTER] to exit")

