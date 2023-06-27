def get_pair_less_than_x(array,X):
    """find pair whose sum equal to X
    
    Keyword arguments:
    array -- list of interger
    X     -- constaant   
    
    Returns a tuple (X,pair[0],pair[1])
    """
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] + array[j] == X:
            return X,array[i], array[j]
        if array[i] + array[j] > X :
            j -= 1
        else:
            i +=1        
arr = sorted([2, 3, 5, 8, 9, 10, 11])
# value to search
VAL = 15
result = get_pair_less_than_x(arr,VAL)
assert result == (15, 5, 10)
print(f"successfully found pair {result[1], result[2]} agaisnt the sum {result[0]}")
