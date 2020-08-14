#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# source == start
# destination == next airport
# first flight has source == NONe
# final flight has source == None
# start with None, match destination with source, add to route
# match prev.destination to next.source, add destination to route
# repeat / use links

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # empty cache to keep track
    cache = {}
    route = [None] * length

    # loop through tickets list to assign source to destination
    for tx in tickets:
        cache[tx.source] = tx.destination
        # print("source", tx.source)
        # print("destination", cache[tx.source])

    # to compare and find NONE, will be overwritten if not NONE
    dest = cache["NONE"]
    print(cache)
    # loop through each index through route
    for i in range(length):
        print("dest", dest)
        route[i] = dest
        dest = cache[dest]

    return route
