def most_frequent_item_count(collection):
    result = 0

    for i in range(len(collection)):
        counter = 0

        for j in range(len(collection)):
            if collection[i] == collection[j]:
                counter += 1

        if counter > result:
            result = counter

    return result