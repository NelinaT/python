def no_it_isnt(list_of_values):
    result_list = []
    reversed_list_of_values = reversed(list_of_values)

    for i in reversed_list_of_values:
        if isinstance(i, bool):
            result_list.append(not i)
        elif isinstance(i,(int, float)):
            result_list.append(- i)
        elif isinstance(i, str):
            result_list.append(i[:: -1])

    return result_list

# print(no_it_isnt([1, -3.14, True, 'abc', 0]))

