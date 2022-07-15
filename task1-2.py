import os


file_path = os.path.join(os.getcwd(), 'recipes.txt')


def cook_book_dict(file_obj):
    cook_book = {}
    with open(file_path, "r", encoding="utf-8") as file_obj:
        for dish in file_obj:
            dishes = dish.strip()
            ingredients = int(file_obj.readline())
            dishes_list = []
            for ing in range(ingredients):
                ingredient_name, quantity, measure = file_obj.readline().split("|")
                dishes_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
            cook_book[dishes] = dishes_list
            file_obj.readline()
    return cook_book


print(cook_book_dict(file_path))


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cook_book_dict('cook_book')
    ingredients_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                if ingredients['ingredient_name'] in ingredients_list:
                    ingredients_list[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
                else:
                    ingredients_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                        'quantity': int(ingredients['quantity'] )* person_count}
        else:
            print(f'{dish} нет в списке')

    return ingredients_list


print(get_shop_list_by_dishes(['Омлет'], 4))
print(get_shop_list_by_dishes(['Фахитос'], 2))
get_shop_list_by_dishes(['Цук'], 2)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))




