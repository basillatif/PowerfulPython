numbers = [7, 4, 11, 3]
#iter() is a generator method
#<list_iterator object at 0x10b473e20>
print(iter(numbers))
print('')
names = ["Tom", "Shelly", "Garth"] 
names_it = iter(names)
print("next(names_it):",  next(names_it))
print("next(names_it):",  next(names_it))
print("next(names_it):",  next(names_it))

#2.4 Python is filled with Iterators
calories = { "apple": 95,
"slice of bacon": 43, "cheddar cheese": 113,
"ice cream": 15, # You wish!
}
items = calories.items()
print('type(items)', type(items))
len(items)
calories['orange'] = 50
print(('orange', 50) in items)
print(('orange', 20) in items)
