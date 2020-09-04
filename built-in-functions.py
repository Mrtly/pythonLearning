# https://docs.python.org/3/library/functions.html

# numeric

x = '47'
y = int(x)
# there is: float(will give 47.0), abs(will keep the - if negative) 
# divmod(x, 3), returns a tuple, (15, 2), 2 is remainder

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')


# strings

s = 'Hello, World'
print(repr(s)) # representation

# ascii(), chr(), ord()

# container functions

x = (1, 2, 3, 4, 5) # a tuple
y = x
# y = reversed(x) -> iterator/object
# but do list(y) to give the reversed list
print(x)
print(y)

# other: sum(), sum(x, y), max(), min(), any(), all()
# z = zip(x, y)

# enumerate

animals = { 'cat', 'dog', 'rabbit'}
for i, v in enumerate(animals): print(f'{i} : {v}')

# functions for objects & classes:
# type(x) gives the type
# isinstance() returns t/f
# id(x) returns numerical id