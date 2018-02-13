# a = [2, 4, 3, 5, 1]
# # print(a[2:].index(a[1]))
# # print(a.index(a[1]))
# def firstDuplicate(a):
#     seen=set()
#     result=[]
#     for idx, item in enumerate(a):
#         if item not in seen:
#             seen.add(item)  # First time seeing the element
#         else:
#             result.append(idx)  # Already seen, add the index to the result
#     if len(result) > 0:
#         return a[result[0]]
#     else:
#         return -1

    # i=0
    # new_index = 0
    # new_list = []
    # while i < len(a):
    #     if a[i] in a[i+1:]:
    #         new_index = a.index(a[i])
    #         new_list.append(a.index(a[i]))
    #     i += 1
    # print(new_list)
    # if len(new_list) > 0:
    #     return a[min(new_list)]
    # else:
    #     return -1


# firstDuplicate(a)

inputArray = [3, 6, -2, -5, 7, 3]
def adjacentElementsProduct(inputArray):
    i = 0
    products = []
    largestnumber = -10000
    for n in inputArray:
        while i <len(inputArray)-1:
            if inputArray[i] * inputArray[i + 1] > largestnumber:
                largestnumber = inputArray[i] * inputArray[i + 1]
                products = [inputArray[i],inputArray[i + 1]]
            i += 1
        return products

print(adjacentElementsProduct(inputArray))

# return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
# this the best solution