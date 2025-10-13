def merge_list(list1,list2):
    # loop each list and check elements
        # if element is not an int, raise typeError
    for elem in list1:
        if not isinstance(elem,int):
            raise TypeError("Your list1 should only have integers.")

    for elem in list2:
        if not isinstance(elem,int):
            raise TypeError("Your list2 should only have integers.")
        
    merged_list = list1 + list2 # unsorted list. We will sort and return this list

    # loop and fill in array with each element
    # check for out-of-bounds when one of the lists is shorter 
    # insertion sort algorithm
    for i in range(1, len(merged_list)):
        comp = merged_list[i] # current element to place
        j = i -1
        # shiffitng larger elements by one
        while j >= 0 and merged_list[j] > comp:
            merged_list[j + 1] = merged_list[j] 
            j -= 1
        merged_list[j + 1] = comp # place item
    return merged_list