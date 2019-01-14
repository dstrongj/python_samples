import sys
import pprint
#this package prints lists one per line

# function for dog years
def dog_years(name, age):
  dog_age = age * 7
  return name.title() + ", you are " + str(dog_age) + " years old in dog years"
print(dog_years(name, age))

#empty list
list_of_dogs = []

#loops through list until length of list == 4
while len(list_of_dogs) < 4:
    age = int(input("How old is your dog? "))
    name = input("What is your dogs name? ")
    list_of_dogs.append(dog_years(name,age))
    if len(list_of_dogs) == 4:
        break

pprint.pprint(list_of_dogs)