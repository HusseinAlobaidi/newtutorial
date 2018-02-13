# import random
#
# random_list = []
# list_length = 20
#
# while len(random_list) < list_length:
#   random_list.append(random.randint(0,10))
#
# count_list = [0] * 11
# index = 0
# count = 0
#
# while index < len(random_list):
#   number = random_list[index]
#   count_list[number] = count_list[number] + 1
#   index = index + 1
#
#
#   print(count_list)
#   print(sum(count_list))

s = [2, 5, 7, 9]
for idx,n in enumerate(s):
  while n[idx + 1] > 0:
    n[idx] += n[idx]
    n[idx +1] -= 1