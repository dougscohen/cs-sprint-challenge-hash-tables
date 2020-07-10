#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


dictionary = {}

def reconstruct_trip(tickets, length):
    """
    Returns the correct route of all your trips.
    
    Parameters:
            tickets (list): list of Ticket class instances
            length (int): length of tickets
    
    Returns:
            routes (list): list of strings that shows entire route of trip
    """
    # loop through array and put tickets in a dictionary,
    #. key = source, value = destination
    for ticket in tickets:
        dictionary[ticket.source] = ticket.destination
    
    # empty list that will hold our route
    route = []
    
    # starting location is place where our source is "NONE"
    start_location = dictionary['NONE']
    # append this starting location to routes
    route.append(start_location)
    
    current_source = dictionary["NONE"]
    
    # while loop
    while True:
        destination = dictionary[current_source]
        
        # TBC: if destination is NONE then we've reached the end of the list
        if destination == "NONE":
            # append the destination to routes and break the loop
            route.append(destination)
            break

        # append the destination to routes
        route.append(destination)
        # update current_source and continue the loop
        current_source = destination
    
    return route