Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.forward(50)
>>> t.left(90)
>>> t.left(360)
>>> t.forward(50)
>>> t.left
<bound method Turtle.left of <turtle.Turtle object at 0x1050f7950>>
>>> 
>>> 
>>> 
>>> 
>>> t.left(90)
>>> t.forward(50)
>>> t.right(270)
>>> t.forward(50)
>>> t.left(180)
>>> t.right(90)
>>> t.reset()
>>> t.up
<bound method Turtle.penup of <turtle.Turtle object at 0x1050f7950>>
>>> t.up()
>>> t.down()
>>> backward(100)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    backward(100)
NameError: name 'backward' is not defined
>>> t.backward(100)
>>> t.up()
>>> t.right(90)
>>> t.forward(20)
>>> t.left(90)
>>> t.down()
>>> t.forward
<bound method Turtle.forward of <turtle.Turtle object at 0x1050f7950>>
>>> t.forward(100)
>>> t.reset()
>>> t.forward(50)
>>> t.forward(70)
>>> t.reset
<bound method Turtle.reset of <turtle.Turtle object at 0x1050f7950>>
>>> t.reset()
>>> t.forward(70)
>>> t.up()
>>> t.forward(50)
>>> t.left(90)
>>> t.left(180)
>>> t.down(50)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t.down(50)
TypeError: pendown() takes 1 positional argument but 2 were given
>>> t.forward(50)
>>> t.down()
>>> t.forward(70)
>>> t.up()
>>> t.forward(50)
>>> t.left(90)
>>> t.left(180)
>>> t.forward(50)
>>> t.forward(70)
>>> t.back(70)
>>> t.down()
>>> t.forward(70)
>>> t.up()
>>> t.forward(50)
>>> t.right(90)
>>> t.forward(50)
>>> t.down()
>>> t.forward(70)
>>> t.up()
>>> t.right(90)
>>> t.forward(50)
>>> t.down()
>>> t.forward(50)
>>> t.right(90)
>>> t.forward(50)
>>> t.right(90)
>>> t.forward(50)
>>> t.right(90)
>>> t.forward(50)
>>> 
