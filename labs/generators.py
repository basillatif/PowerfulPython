'''
>>> evens = evens_up_to(8)
>>> type(evens)
<class 'generator'>
>>> for even in evens:
...     print(even)
2
4
6
8

>>> squares = squares_up_to(16)
>>> type(squares)
<class 'generator'>
>>> for square in squares:
...     print(square)
1
4
9
16

>>> for square in squares_up_to(15):
...     print(square)
1
4
9

>>> counter = countdown(3)
>>> type(counter)
<class 'generator'>
>>> for count in countdown(3):
...     print(count)
3
2
1
BLASTOFF!

>>> for count in countdown(10):
...     print(count)
10
9
8
7
6
5
4
3
2
1
BLASTOFF!

'''

# Write your code here:

#evens = evens_up_to(8)
def evens_up_to(ceiling):
    num = 2
    while num<=ceiling:
        yield num
        num += 2

def squares_up_to(ceiling):
    num, square = 1, 1
    while square <= ceiling:
        yield square
        num += 1
        square = num ** 2

def countdown(start):
    while start > 0:
        yield start
        start -= 1
    yield "BLASTOFF!"
# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# From Powerful Python. Copyright MigrateUp LLC. All rights reserved.

