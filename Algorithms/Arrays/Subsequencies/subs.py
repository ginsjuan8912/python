arr1 = [5, 1, 22,22, 25, 6, -1, 8, 10]
arr2 = [5, 1, 22, 22, 25, 6, -1, 8, 10]


def isValidSubsequence(array , sequence):
    #Check for an empty array and sequence
    if((len(array) <= 0 or len(sequence) <= 0)):
        return False
    
    #Check if the sequence is a subset of the array
    if not (set(sequence).issubset(set(array))):
        return False
    
    upper_index = len(sequence)
    last_index = 0

    for i in range(0,len(sequence),1):

        next_inx = i+1
        if(i+1 >= upper_index):
            break
       
        
        lower_idx = search(array, sequence, i, last_index)
        last_index = lower_idx
        next_inx = search(array, sequence, next_inx, last_index) 

        if not( lower_idx <= next_inx):
            return False
        
    
    return True


def search(array, sub_array, index: int, last_index: int = 0) -> int:
    
    try:
        return array.index(sub_array[index],last_index + 1)
    except:
        return -1


print(isValidSubsequence(arr1, arr2))


