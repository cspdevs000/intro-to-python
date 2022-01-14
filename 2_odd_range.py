def odd_range(end):
    arr = []
    for i in range(1, end, 2):
        arr.append(i)
    return arr

print(odd_range(13))
print(odd_range(6))