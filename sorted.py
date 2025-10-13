# dictest = { 'Ana' : (5464512, 24) , 'Michael' : (5446987, 32) , 'Tom' : (1557896, 20)}


def reverse_sort_dictionary(dictionary):

    keys_list = [] # list with all keys
    # getting keys from dict
    for key in dictionary:
        keys_list.append(key)

    # reverse sorting the list of keys
    keys_list.sort(reverse=True)

    tuple_list = [] # list with tuples we are returning

    # looping using the list and getting the elements in the dictionary
    for i in range(len(keys_list)):
        element_key = keys_list[i]
        dict_element = dictionary[element_key]
        tuple_list.append((element_key, dict_element[0])) # dict_element[0] gets phone number in tuple 
    
    return tuple_list

