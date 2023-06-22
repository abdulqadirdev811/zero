def insertion_sort(unsorted_list):
    for i,el in enumerate(unsorted_list):
        j = i - 1
        while j > 0 and el < unsorted_list[j] :
            unsorted_list[j+1] = el
            unsorted_list[j] = el
    


unsorted_list = [1,2,3,4]
insertion_sort(unsorted_list)