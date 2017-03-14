Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> sports = {'Mike':'football','Mushell':'Ice hocey', 'Rebecca' : 'Netball'}
>>> sports['Mike'] = 'Ice hockey'
>>> print (sports)
{'Mushell': 'Ice hocey', 'Rebecca': 'Netball', 'Mike': 'Ice hockey'}
>>> colors = {'Red','Blue','Ornge'}
>>> sports + colors
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sports + colors
TypeError: unsupported operand type(s) for +: 'dict' and 'set'
>>> GAMES = {'TC.Ranbow 6 vagas 2','pokeen tornement','Smash bros'}
>>> 
>>> FOOD = {'Taco','Hamberger','Well done STAKE'}
>>> GAMES+FOOD
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    GAMES+FOOD
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> favrots = GAMES + FOOD
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    favrots = GAMES + FOOD
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> 3*25
75
>>> 40*2
80
>>> 80*75
6000
>>> hello = "wut up, im Gavin Pennycuff"
>>> print (hello)
wut up, im Gavin Pennycuff
>>> 
