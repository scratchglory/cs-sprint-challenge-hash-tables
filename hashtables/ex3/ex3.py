# find the number that exists in all lists
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # intersection array
    result = []
    cache = {}
    # loop through first arr
    for arr in arrays:
        # loop through to get to indexs
        for i in arr:
            if i not in cache:
                cache[i] = 1
                # print("cache", cache)
            else:
                # add to result
                result.append(i)
                # print("else cache", result)

    # result will have the duplicates
    # .fromkeys(): returns a dictionary with the specified keys and specified value
    # print("result", result)
    result = list(dict.fromkeys(result))
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
