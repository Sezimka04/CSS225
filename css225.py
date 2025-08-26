Last login: Thu Jul 17 15:28:45 on ttys004
sezimmamatova@Sezims-MacBook-Air ~ % python3
Python 3.9.6 (default, Nov 10 2023, 13:38:27) 
[Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> # 1 - integer
>>> n = 5, 7, 2
>>> # 2 - float
>>> m = 4.2, 7.5, 1.8
>>> # 3 - boolean
>>> 4>3
True
>>> 8<5
False
>>> # 4 - tring
>>> o = "My name is Sezim"
>>> p = "and I want to be a programmer"
>>> print(o,p)
My name is Sezim and I want to be a programmer
>>> # 5 - list
>>> baking_ingredients = ["suger", "flour", "egg", "milk"]
>>> print(type(n))
<class 'tuple'>
>>> print(type(m))
<class 'tuple'>
>>> print(type(o))
<class 'str'>
>>> print(type(p))
<class 'str'>
>>> print(type(baking_ingredients))
<class 'list'>
>>> # adding element to the list
>>> superheros = ["Wonder women", "Batman", "Flash"]
>>> superheros.addend("Superman")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'addend'
>>> superheros.append("Superman")
>>> print(superheros)
['Wonder women', 'Batman', 'Flash', 'Superman']
>>> ø
