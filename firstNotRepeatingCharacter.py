def firstNotRepeatingCharacter(s):
    order = []
    counts = {}
    for x in s:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            order.append(x)
    for x in order:
        if counts[x] == 1:
            return x
    return "'_'"


s='abacabad'
print(firstNotRepeatingCharacter(s))

# while s != '':
#         ch = s[0]
#         length = len(s)
#         s = s.replace(ch,'')
#         if length - len(s) == 1:
#             return(ch)
#     return('_')


# from collections import Counter
#
# def firstNotRepeatingCharacter(s):
#     counts = Counter(s)
#     for character in s:
#         if counts[character] == 1:
#             return character
#     return "_"

