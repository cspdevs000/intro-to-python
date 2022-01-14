#arrays are still called lists in python

numbers = [1, 2, 3, 4]
def double_number(num):
    return num + num

result = map(double_number, numbers) #<--can wrap this value in list too
print(result) #prints an object id
print(list(result)) #prints the actual list

result2 = map(lambda x: x + x, numbers)
print('result 2', list(result2))

result3 = list(map(lambda y: y * y, numbers))
print('result 3', result3)


def triple_number(num):
    return num + num + num
result_triple = list(map(triple_number, numbers))
print ('result tripled', result_triple)

anom_triple = list(map(lambda z: z + z + z, numbers))
print ('result tripled w anonymous', anom_triple)



numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result4 = map(lambda x, y: x + y, numbers1, numbers2)
print('result 4', list(result4))





# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result5 = filter(lambda x: x % 2 != 0, seq)
# print(list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
result6 = filter(lambda x: x % 2 == 0, seq)
# print(list(result6)) # [0, 2, 8]




folks = [14, 17, 19, 20, 22, 29, 32, 34, 37]


def grown_folks(age):
    if age >= 21:
        return True
    else:
        return False
old_array = list(filter(grown_folks, folks))
print('these ones are old', old_array)


young_array = list(filter(lambda x: x < 21, folks))
print('these are the youngins', young_array)