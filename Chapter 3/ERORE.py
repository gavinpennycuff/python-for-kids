Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> tuple_try_out = (0,1,2,3)
>>> print (tuple_try_out)
(0, 1, 2, 3)
>>> fibs[1] = 7
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fibs[1] = 7
NameError: name 'fibs' is not defined
>>> tuple_try_out[1] = 7
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tuple_try_out[1] = 7
TypeError: 'tuple' object does not support item assignment
>>> list2 = [1,2,3,4,1,2,3,4]
>>> list1 / 20
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list1 / 20
NameError: name 'list1' is not defined
>>> list2 / 20
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list2 / 20
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> list2 -20
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list2 -20
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> list2 + 50
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list2 + 50
TypeError: can only concatenate list (not "int") to list
>>> sports = ['Ralph Williams, Football','Michael Tippentt, Basketball','Edward Elgar, Bascball','Rebecca Clarke, Netball','Ethel Smyth, Badminton']
>>> 
