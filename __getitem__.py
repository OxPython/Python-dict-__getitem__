'''
Created on Jul 2, 2014

@author: viejoemer

Are there other ways to get data from a dictionary in Python?

¿Hay otras maneras de obtener datos de un diccionario en Python?

Python has a __getitem__ special method to get a items in a dictionary.
'''

#Definition of a dictionary
d = {'three': 3, 'two': 2, 'one': 1}
print(d)

#get a value traditional.
value = d['two']
print(value)

#Using a special method __setitem__
value = d.__getitem__("one")
print(value)

#Definition of a dict into an other dict
d = {'one': {'two': 2}}
print(d)

#get a value.
value = d['one']
print(value)

#get a value.
value = value['two']
print(value)

#get the value in one line.
value = d['one']['two']
print(value)