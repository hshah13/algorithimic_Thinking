def inversion(array_list):

    inversion_list = []
    for idx in range(0, len(array_list)):
        for idx2 in range(idx + 1, len(array_list)):
            if array_list[idx] > array_list[idx2]:
                inversion_list.append((array_list[idx], array_list[idx2]))
                
    return inversion_list


print inversion([5, 4, 3, 6, 7])