def cook_dict():
    with open('recipes.txt', encoding='utf-8') as recipes:
        cook_book = {}
        while True:
            try:
                cook_book.setdefault(recipes.readline().strip(), [{'ингредиент': stat[0],
                                                                   'количество': int(stat[1]),
                                                                   'ед. измерения': stat[2].strip()}
                                                                  for stat in [recipes.readline().split(' | ')
                                                                  for _ in range(int(recipes.readline()))]])
                recipes.readline()
            except:
                break

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for dish in dishes:
        if dish in cook_dict().keys():
            for i in cook_dict()[dish]:
                if i['е'] in all_ingredients.keys():
                    all_ingredients[i['е']]['количество'] += i['количество']*person_count
                else:
                    all_ingredients.setdefault(i['е'], {'ед. измерения': i['ед. измерения'], 'количество': i['количество']*person_count})

    print(all_ingredients)


def start():
    dishes = input('Введите названия блюд через пробел: ').split()
    persons = int(input('Введите количество персон: '))
    get_shop_list_by_dishes(dishes, persons)


start()