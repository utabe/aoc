ingredients = set()
ingredients_count = []
allergens = {}

for line in open('input.in').readlines():
    ingreds, allerg = line.strip().split(' (contains ')
    ingreds = ingreds.split()
    allerg = allerg[:-1].split(', ')
    ingredients.update(set(ingreds))
    ingredients_count.extend(ingreds)
    for a in allerg:
        if a not in allergens:
            allergens[a] = set(ingreds)
        else:
            allergens[a] &= set(ingreds)
unsafe_ingredients = set()
for v in allergens.values():
    unsafe_ingredients.update(v)
for _ in range(len(allergens)):
    for a, i in allergens.items():
        if len(i) == 1:
            for ingredient, allergy in allergens.items():
                if allergy != i:
                    allergens[ingredient] = allergy - i

allergens_reverse = {v.pop(): k for k, v in allergens.items()}
safe_ingredients = ingredients - unsafe_ingredients
print(sum(ingredients_count.count(i) for i in safe_ingredients))
print(*sorted(list(unsafe_ingredients),key=lambda x: allergens_reverse[x]),sep=',')