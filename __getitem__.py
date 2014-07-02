'''
Created on Jul 2, 2014

@author: viejoemer

Are there other ways to get data into a dictionary in Python?

¿Hay otras maneras de obtener datos en un diccionario en Python?

Python has a __getitem__ special method to get a items in a dictionary.
'''

#Definition of a dictionary
d = {'three': 3, 'two': 2, 'one': 1}
print(d)

#Using a special method __setitem__
value = d.__getitem__("one")
print(value)