from pprint import pprint

with open('file.txt', 'r', encoding='utf-8') as file:
    cook_book = {}

    for line in file:
        data3 = []
        dish = line
        quantity = int(file.readline())
        for i in range(quantity):

            lines = []
            data = file.readline().strip().split('|')
            lines.append(data)

            for l in lines:
                data2 = {'ingredient_name': l[0], 'quantity': l[1], 'measure': l[2]}
                data3.append(data2)
            cook_book[line.strip()] = data3

            # print(data3)
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    for dish in dishes:

        for dish_name in cook_book:
            if dish == dish_name:
                for i in cook_book[dish]:
                    ing_name = i['ingredient_name']
                    quantity = int(i['quantity'])
                    measure = i['measure']
                    if ing_name not in ingredients_list:
                        quantity *= person_count
                        ingredients_list[ing_name] = {'quantity': quantity, 'measure': measure}
                    else:
                        ingredients_list[ing_name]['quantity'] += quantity * person_count

    pprint(ingredients_list, sort_dicts=False)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)