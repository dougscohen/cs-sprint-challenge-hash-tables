def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # sort the array from largest to smallest
    a.sort(reverse=True)
    
    # empty dictionary where key = positive number, and value = negative number
    dictionary = {}
    
    # loop through array
    for item in a:
        # if item is positive, add it as a key in the dictionary
        if item > 0:
            dictionary[item] = None
        
        # if item is negative, see if its positive counterpart is already in
        #. dictionary
        if item < 0:
            if abs(item) in dictionary:
                
                # if it is, add it as the value for its positive key
                dictionary[abs(item)] = item
    
    # list that will contain positive numbers that have a negative counterpart
    result = []
    
    # loop through the dictionart
    for key, value in dictionary.items():
        
        # if value is not None, it means that key:value pair contains a
        #. positive number and its negative counterpart
        if value != None:
            
            # append the key (positive number)
            result.append(key)

    # results are in descending order, so lets sort it (preference)
    result.sort()
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
