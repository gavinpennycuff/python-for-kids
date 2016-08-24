Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> sports = ['Ralph Williams, Football','Michael Tippentt, Basketball','Edward Elgar, Bascball','Rebecca Clarke, Netball','Ethel Smyth, Badminton','Frank Bridge' : 'Rugby']
SyntaxError: invalid syntax
>>> ['Ralph Williams, Football','Michael Tippentt, Basketball','Edward Elgar, Bascball','Rebecca Clarke, Netball','Ethel Smyth, Badminton','Frank Bridge, Rugby']
['Ralph Williams, Football', 'Michael Tippentt, Basketball', 'Edward Elgar, Bascball', 'Rebecca Clarke, Netball', 'Ethel Smyth, Badminton', 'Frank Bridge, Rugby']
>>> sports = ['Ralph Williams, Football','Michael Tippentt, Basketball','Edward Elgar, Bascball','Rebecca Clarke, Netball','Ethel Smyth, Badminton','Frank Bridge, Rugby']
>>> sports = {'Ralph Williams' : 'Football','Michael Tippentt' : 'Basketball','Edward Elgar' : 'Bascball','Rebecca Clarke' : 'Netball','Ethel Smyth' : 'Badminton','Frank Bridge' : 'Rugby'}
>>> print (sports['Ralph Williams'])
Football
>>> del sports['Ethal Smyth']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    del sports['Ethal Smyth']
KeyError: 'Ethal Smyth'
>>> 
