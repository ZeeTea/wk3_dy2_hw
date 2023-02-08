#Filter out all of the empty strings from the list below</p>

#`Output: ['Argentina', 'San Diego', 'Boston', 'New York']`

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

filtered_places = list(filter(lambda place: place.strip(), places))

print(filtered_places)

#Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"

#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda x: x.split()[-1])

print(author)

#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

farhenheit = list(map(lambda x: (x[0], (9/5)*x[1]+32), places))

print(farhenheit)

#Write a recursion function to perform the fibonacci sequence up to the number passed in.

#Output for fib(5) => 
#Iteration 0: 1
#Iteration 1: 1
#Iteration 2: 2
#Iteration 3: 3
#Iteration 4: 5
#Iteration 5: 8

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(6):
    print("Iteration", i, ":", fib(i))