import sort_list_of_sets
from sort_list_of_sets import change_list_element_datatype,sort_multidimentional_array

list_of_set1 = [{2, 3},{5, 6},{1, 14},{9,15}, {12,14} ]
multidimentional_array = change_list_element_datatype(list_of_set1,list) # we want to convert set to list as sets are not subscriptable
rslt = sort_multidimentional_array(multidimentional_array)
sorted_list_of_sets = change_list_element_datatype(rslt,set) # converting the list of arrays to  the list of sets
print("sorted_list_of_sets1 >> ",sorted_list_of_sets)
assert sorted_list_of_sets == [{1, 14}, {2, 3}, {5, 6}, {9, 15}, {12, 14}]
print("Sorted data successfully [!]")