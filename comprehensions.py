# nums = [1,2,3,4,5]
# my_list = [n for n in nums]
# print(my_list)

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

names = ['bruce', 'clark', 'peter', 'logan', 'wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# z = dict(zip(names, heroes))
# print(z)

my_dict = {name : hero for name,hero in zip(names,heroes) if name != 'peter'}
print(my_dict)
