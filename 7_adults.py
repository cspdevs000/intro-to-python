ppl = [
  {'name': 'Khalid Robinson', 'age': 22},
  {'name': 'Ariel Winter', 'age': 20},
  {'name': 'Post Malone', 'age': 25},
  {'name': 'Willow Smith', 'age': 17}
]

def adults(people):
    names = []
    for i in range(len(people)):
        person = people[i]
        if person['age'] >= 18:
            names.append(person['name'])
    return names

print(adults(ppl))