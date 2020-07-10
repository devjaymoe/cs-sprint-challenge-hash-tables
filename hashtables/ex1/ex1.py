def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    found_pair = []

    for i in range(length):

        cur_weight = weights[i]

        if cur_weight not in cache:
            cache[cur_weight] = [i]
        else:
            cache[cur_weight].append(i)

        remaining_value = limit - cur_weight

        if remaining_value in cache:
            
            if len(cache[remaining_value]) > 1:

                return sorted(cache[remaining_value], reverse=True)

            if cache[remaining_value] is not cache[cur_weight]:
   
                found_pair.append(cache[remaining_value][0])
                found_pair.append(cache[cur_weight][0])
                return sorted(found_pair, reverse=True)

    return None