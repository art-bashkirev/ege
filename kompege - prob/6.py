from turtle import *

k = 10
up()
speed("fastest")
delay(0)

for x in range(-10, 24):
    for y in range(-10, 20):
        goto(x * k, y * k)
        dot()
home()
down()

#begin_fill()

for _ in range(3):
    forward(27 * k)
    right(90)
    forward(12 * k)
    right(90)
up()
fd(4 * k)
rt(90)
fd(6 * k)
lt(90)
down()
for _ in range(3):
    fd(83 * k)
    rt(90)
    fd(77 * k)
    rt(90)

#end_fill()
done()