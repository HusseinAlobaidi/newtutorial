def find_last(search_string, target_string):
    if search_string.find(target_string) == -1:
        return -1
    current_location = 0
    while current_location >= 0:
        last_location = current_location
        current_location = search_string.find(target_string, current_location + 1)
    return last_location


print(find_last('11111', 'a'))
