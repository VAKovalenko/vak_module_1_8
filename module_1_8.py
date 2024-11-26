my_dict = {'Измаил': 1990, 'Венера': 1994, 'Римма': 2004, 'Руслан': 2003}
print(my_dict)
print(my_dict['Руслан'])
print(my_dict.get('Рустем'))
my_dict.update({'Европа': 2000,
               'Антоний': 2010})
print(my_dict)
rimma_pop = my_dict.pop('Римма')
print(rimma_pop)
print(my_dict)

my_set = {1, 2, 2, 3, 'строка', 3, 3, 4, 4, 'строка', 4, 4, 8.75}
print(my_set)
my_set.add(9)
my_set.add('stringer')
my_set.remove(1)
print(my_set)
