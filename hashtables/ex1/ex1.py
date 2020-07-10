# empty dictionary to hold data
dictionary = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    Function that takes in a list of weights (weights), the length of the list
    (length), an integer weight limit (limit) and finds two indeces whose sum
    of weights equals the weight limit.
    
    Parameters:
            weights (list): list of integer weights
            length (int): length of the weights list
            limit (int): package weight limit
            
    Returns:
            two indeces whose sum of weights equals the weight limit.
    """
    
    # store the weights as keys, and their indexes as the value
    for i, weight in enumerate(weights):
        dictionary[weight] = i

    # loop through all the weights
    for index, weight in enumerate(weights):
        
        # 'needed' weight that would cause sum equal the limit
        needed = limit - weight
        current_weight_index = index
        
        # see if the needed weight is in the dictionary as a key
        if needed in dictionary:
            
            # grab its index
            needed_weight_index = dictionary[needed]
            
            # and return a tuple of the needed weight and the current
            #. index we are looping through, with the higher index first
            return (max(current_weight_index, needed_weight_index),
                    min(current_weight_index, needed_weight_index))

    # Otherwise, there isn't a second weight that adds up to equal the limit
    return None
