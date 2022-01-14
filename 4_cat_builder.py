
def cat_builder(name, color, toys):
    cat = {}
    cat['name'] = name
    cat['color'] = color
    cat['toys'] = toys
    return cat

cat_1 = cat_builder('Garfield', 'golden', ['scratching-post', 'yarn'])
print(cat_1)

cat_2 = cat_builder('Whiskers', 'rainbow', ['poptarts'])
print(cat_2)
