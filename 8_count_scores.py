ppl = [ 
    {'name': "Pete", 'score': 10},
    {'name': "Mike", 'score' : 10},
    {'name': "Pete", 'score': -8},
    {'name': "Dexter", 'score': 12}
]

def count_scores(people):
    scores_obj = {}

    for person in people:
        name = person.get('name')
        score = person.get('score')
        print(name)

        if (scores_obj.get(name)):
            scores_obj[name] += score
        else:
            scores_obj[name] = score

    return scores_obj

print(count_scores(ppl))