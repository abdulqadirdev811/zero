def sort_multidimentional_array(list_of_dictionary):
    return sorted(list_of_dictionary,key = lambda x : x[0])


def change_list_element_datatype(input_list,data_type):
    resultant_array = [data_type(i) for i in input_list]
    return resultant_array

