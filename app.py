# this is how you comment tings out
# undefined in python is None
# and / or are just and / or
# use help(str) or help(list) etc to get in-terminal documentation for built in methods

name = 'cameron'
# print(name)

nothing = None
is_working = True
car_off = False

if is_working and car_off:
    print('This is true')
    num = 7
    print('Car is off')
elif nothing:
    print('else if')
else: 
    print('This is not true')
# indentation is very important... ^ above code wouldn't run if indented differently

if is_working:
    print('This is working also')

print(15/6)
print(15//6) #doesn't round, just slices decimal off
#exponents
print(2**4)

card1 = "Ace of Spades"
print(card1.split(" "))
print(card1.upper())
print(card1.lower())
print(card1.index('s')) #is case sensitive, only prints first instance
print(card1.replace("Spades", "Hearts")) #replaces all instances of first value
print(len(card1))
print("Spades" in card1) #searches the string

string="it was a sunny day"
print(string[3]) #chooses inex
print(string[-2]) #chooses index counting backwards
print(string[3:7]) #gets a range of indeces
print(string[:3]) #gets everything before stated index
print(string[4:]) #gets everything after stated index
print(string[::-1]) #reverses starting from stated index
print(string[::2]) #gets every other index

# == for equals
# != for not equals
# not, or, and are all literal

#arrays are called lists
numlist = [1,2,3,4,5,6]
print(len(numlist))

randomlist = [1,'two', 3, 'four', True, False, 'hi']
print(len(randomlist))
print(randomlist[1])
print(randomlist[-1])

five_trues = [True] * 5
print(five_trues)
five_zeros = [0] * 5
print(five_zeros)

zero_through_ten = list(range(11))
print(zero_through_ten)

a = [213, 214214, 12, 21, 3525, 1, 563]
a.sort()
print(a)
a = a[::-1] #reverses the list order
print(a)
a.append(0)
print(a)
zero = a.pop() #actually removes the index from the list
print(zero)
print(a)

#insert value into specific index
a.insert(2,666) #first value is where you want it to go
print(a)

if 666 in a:
    print("yas")

#objects are called dicitionaries
#keys that are strings must be in quotes 
cat = {
    'name': 'Napkin',
    'breed': "monster",
    'fav_food': 'bikki'
}
print(cat['name'])
print(cat['fav_food'])
print(cat.get('breed'))
cat['name'] = 'Carmella'
print(cat['name'])
#dot notation doesn't work like js objects
#can add keys/values to the object later on
cat["age"] = 6
print(cat['age'])
print('items', cat.items())
#item returns the key / values as tuples
print('keys', cat.keys())
cat_keys = list(cat.keys()) #puts it in array
print(cat_keys)

#type conversion
int('42')
str(42)
float(42)
bool(42)
bool(-1)
bool('foo')
bool('')


#string interpolation
# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}th state to join the union in {year}."
# print(my_message)


location = 'New York City'
numero = 1
introduction = "{} is the number {} city for covid spreading".format(location, numero)
print(introduction)

group = 'Beastie Boys'
adjective = 'annoying'
location_2 = 'the world'
statement = f"The {group} are the most {adjective} rappers in {location_2}"
print(statement)

def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"

state = "Washington State" #if this was indented over it would be inside above function
year = 1889
n = 42
my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
print(my_message)

# look up garbage collection
# get a book on computer science

# loops

for i in range(0, 10):
  if i % 2 == 0:
    print("{} is even".format(i))
  if i % 2 == 1:
    print("{} is odd".format(i))

# n = 0
# while n < 1000:
#     n+=1
#     if n % 2 == 0:
#         print(f'{n} is even...')

# n = True
# numba = 1
# while n:
#     if n % 2 == 0:
#         print(f'{numba} is even...')

#         if numba == 750:
#             n = False
#             print('end program')
#     numba += 1

# for loop
# for i in range(1, 251):
#     if i % 2 == 0:
#         print(f"{i} is even...")
#         if i == 250:
#             print('end program')

# for i in range(1, 251, 5): # thid argument is the step range
#     if i % 2 == 0:
#         print(f"{i} is even...")
#         if i == 250:
#             print('end program')

# numberz = [213, 214214, 12, 21, 3525, 1, 563]
# for i in range (len(numberz)):
#     element = numberz[i]
#     if element % 2 == 0:
#         print(f"{element} is even...")
#         if element == 563:
#             print('end program')
#         if element == 12:
#             print("hi i'm 12")

students = [
    {
        'name': 'cameron',
        'city': 'new york'
    },
    {
        'name': 'blameron',
        'city': 'blue york'
    },
    {
        'name': 'scrameron',
        'city': 'screw york'
    }
]

for i in range(len(students)):
    student = students[i]
    print(student.get('name'))

for i in range(len(students)):
    student = students[i]
    print(student.get('city'))
    if student.get('city') == 'new york':
        print(f'{student.get("name")} wins a lifetime supply of soylent')

for student in students:
    print(student)

for key in students[0]:
    print('key', key)
    print('value', students[0].get(key))

for key in students[1]:
    print('key', key)
    print('value', students[1][key])

for anything in students[2]:
    print('part 3', anything)
    print('value', students[2][anything])

for key, value in students[0].items():
    print(key, '->', value)
