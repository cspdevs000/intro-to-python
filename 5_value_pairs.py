object1 = {'name': 'One', 'location': 'Remote', 'age': 1}
object2 = {'name': 'Two', 'location': 'San Francisco'}

def value_pair(obj1, obj2, key):
    val_1 = obj1[key]
    val_2 = obj2[key]
    arr = [val_1, val_2]
    return arr

print(value_pair(object1, object2, 'location'))
print(value_pair(object1, object2, 'name'))