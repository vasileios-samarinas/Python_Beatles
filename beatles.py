beatles = [
    {"name": "John Lennon", "birth_year": 1940, "death_year": 1980, "instrument": "piano"},
    {"name": "Paul McCartney", "birth_year": 1942, "death_year": None, "instrument": "bass"},
    {"name": "George Harrison", "birth_year": 1943, "death_year": 2001, "instrument": "guitar"},
    {"name": "Ringo Starr", "birth_year": 1940, "death_year": None, "instrument": "drums"}
]

# Use the `beatles` list above to answer the following questions:

# 1. John Lennon also plays guitar. Access the `instrument` key in his dictionary and change its value:
beatles[0]['instrument']= "guitar"
print(beatles[0])
print(beatles[0:3])

# 2. Write a function which takes in the list of band members as a parameter,
#    and returns a list of all the Beatles' names:
# Expected result: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr']

def names(members):
   return [member['name'] for member in members]

result = names(beatles)
print(result)

# 3. Write a function which takes in the list of band members as a parameter,
#    and returns a list of the members who are still alive
#    (i.e. they have no value for `death_year`)
#    Return the full dictionary for each member
# Expected result: [
#    {'name': 'Paul McCartney', 'birth_year': 1942, 'death_year': None, 'instrument': 'bass'},
#    {'name': 'Ringo Starr', 'birth_year': 1940, 'death_year': None, 'instrument': 'drums'}
# ]

def alivemembers(members):
    return [member for member in members if member['death_year'] == None]

result = alivemembers(beatles)
print(result)


