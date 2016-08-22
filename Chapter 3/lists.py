Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 01:25:11) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> list1 = [1,2,3,4]
>>> list2 = ['I','tripped','over','and','hit','the','floor']
>>> print(list1 + list2)
[1, 2, 3, 4, 'I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
>>> list3 = list1 + list2
>>> print(list3)
[1, 2, 3, 4, 'I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
>>> list12 = [1,2]
>>> print (list12 * 5)
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
>>> mylist = [wizard_list,list3]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    mylist = [wizard_list,list3]
NameError: name 'wizard_list' is not defined
>>> mylist = [list12,list3]
>>> print(mylist )
[[1, 2], [1, 2, 3, 4, 'I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']]
>>> 
