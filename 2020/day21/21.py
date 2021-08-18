from timeit import default_timer as timer

def get_input():
    with open("./day21/21.in","r") as f:
       return  [line.replace(")","").split(" (contains ") for line in f.read().split("\n")]

def p1(data):
    allergens = {}
    occurences = {}
    for food in data:
        for allergen in food[1].split(', '):
            if allergen in allergens:
                allergens[allergen] = [i for i in food[0].split(' ') if i in allergens[allergen]]
            else:
                allergens[allergen] = [i for i in food[0].split(' ')]
        for ingredient in food[0].split(' '):
            if ingredient in occurences:
                occurences[ingredient] += 1
            else:
                occurences[ingredient] = 1
    res = 0
    for ingredient, occur in occurences.items():
        if all(ingredient not in v for v in allergens.values()):
            res += occur
    return res, allergens, occurences

def p2(data, allergens, occurences):
    seen = set()
    # Once lengths are all equal to 1 must be the allergens
    while(any(len(a)>1 for a in allergens.values())):
        for allergen, ingredients in allergens.items():
            if len(ingredients) == 1 and ingredients[0] not in seen:
                seen.add(ingredients[0])
            # Remove Non allergens as only 1 ingredient contains each allergen.
            elif len(ingredients) > 1:
                for s in seen:
                    if s in ingredients:
                        allergens[allergen].remove(s)
    return ",".join([v[0] for k,v in sorted(allergens.items(), key=lambda k:k[0])])

print("Day 21: Allergen Assessment")
data = get_input()
p1start = timer()
p1, all, occ = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data, all, occ)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")