def intersection(arrays):
    """
    Finds the intersection between multiple lists of integers.
    
    Parameters:
            arrays (list): list of lists containing integers
            
    Returns:
            (list): list of numbers that exists in all the lists
    """
    # empty dict to hold data; key = number, value = count
    dictionary = {}
    
    # loop through arrays
    for array in arrays:
        
        # loop through each item in array
        for item in array:
            
            # if item is in the dictionary already, add 1 to the count
            if item in dictionary:
                dictionary[item] += 1
                
            # otherwise, add it as a key and make the count 1
            else:
                dictionary[item] = 1
    
    # empty list that will contain numbers that appear in every array
    result = []
    
    # loop through the pairs in the dictionary
    for data in list(dictionary.items()):
        
        # if the value in each key:value pair equals the length of arrays, we know it
        # appeared in every array
        if data[1] == len(arrays):
            
            # append the key (number) to results
            result.append(data[0])
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
