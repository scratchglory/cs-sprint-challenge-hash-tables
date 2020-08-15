def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}

    print(a)
    for i in a:
        # initialize with adding the is to cache
        cache[i] = 1
    # checking for negative numbers
    for i in a:
        # want to return positive numbers, make sure it is greater than 0 and append to results
        if (i * -1) in cache and i > 0:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
