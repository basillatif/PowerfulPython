#An iterator over a collection is a separate object, with its own identity - which you can verify with id():
numbers = [7, 4, 11, 3]
id(numbers)

#iter() is a generator method
#<list_iterator object at 0x10b473e20>
print(iter(numbers))
#next() - Each time you call it, next(my_iterator) fetches and returns the next element
print('')
names = ["Tom", "Shelly", "Garth"] 
names_it = iter(names)
print("next(names_it):",  next(names_it))
print("next(names_it):",  next(names_it))
print("next(names_it):",  next(names_it))
#2.2 generator objects
def gen_nums(): 
    n=0
    while n < 4:
        yield n 
        n += 1
#2.3Generator Patterns and Scalable Composability

#2.4 Python is filled with Iterators
calories = { "apple": 95,
"slice of bacon": 43, "cheddar cheese": 113,
"ice cream": 15, # You wish!
}
items = calories.items()
print('type(items)', type(items))
print("len(items):", len(items))
print("items: ", items)
calories['orange'] = 50
print("items: ", items)
print( '(\'orange\', 50) in items::', ('orange', 50) in items)
print( '(\'orange\', 20) in items::', ('orange', 20) in items)

foods = calories.keys() 
counts = calories.values()
print('foods: ', foods)
print('counts: ', counts)

#False
print('\'yogurt\' in foods:::', 'yogurt' in foods)
#False
print('100 in counts:::',100 in counts)
calories['yogurt'] = 100 
print("calories: ", calories)
print('\'yogurt\' in foods:::','yogurt' in foods)
print('100 in counts:::',100 in counts)

#Iteration has snuck into many places in Python. The built-in range function returns an iterable:
seq = range (3)
print('type(seq): ', type(seq))
for n in seq: print(n)


#The built-in map, filter, and zip functions all return iterators:
numbers = [1,2,3]
big_numbers = [100,200,300]
def double(n):
    return 2*n
def is_even(n):
    return n % 2 == 0 
mapped = map(double, numbers)
print('mapped: ', mapped)
for num in mapped: print(num)

filtered = filter(is_even , numbers)
for num in filtered: print(num)

zipped = zip(numbers , big_numbers)
print('zipped:', zipped)
for pair in zipped: print(pair)