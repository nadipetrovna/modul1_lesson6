my_dict = {'Bob':1631,'Bill':1756,'Jim':1908,'Kent':1987}
print(f'Мой словарь: {my_dict}')
print(f"Значение: {my_dict['Bob']}")
print(my_dict.get('Nadya', 'Такого элемента не существует'))
my_dict.update({'Nadya':1934,
                'Sara':1938,
                'Vara':1983})
print(f'Обновленный словарь: {my_dict}')
key_my_dict = 'Bill'
print(f'Удаленный элемент: {key_my_dict}, {my_dict.pop(key_my_dict)}')
print(f'Словарь после уделения элемента : {my_dict}')

my_set = {6, 9,True,'string',6.7, 9,45,6, 'string'}
print(f' Коллекция: {my_set}')
my_set.update({2,1.9})
my_set.discard(True)
print(f' Коллекция после добавления и удаления элементов: {my_set}')
