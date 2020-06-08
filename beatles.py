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