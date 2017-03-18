Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> age = 13
>>> if age > 20:
	print('You are to old')

>>> age = 25
>>> if age > 20:
	print('you are to old!')
	print('Why are you here?')
	print('Why aren\'t you mowing a lawn or sorting papers?')

you are to old!
Why are you here?
Why aren't you mowing a lawn or sorting papers?
>>> print(age = 25)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(age = 25)
TypeError: 'age' is an invalid keyword argument for this function
>>> 
