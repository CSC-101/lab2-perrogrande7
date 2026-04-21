def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated? The first Sum
    elif len(L) > 1:                                  #   and what are the values being added? "This" + "Is" + "The"
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated? The First and Second Sums
    elif len(L) > 0:                                  #   and what are the values being added? "s" + "e"
        result = len(L[0])                            # For which call below is this statement evaluated? The first, second, and third sums
    else:                                             # and what are the values being added? "a" + "s" + "this"
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()
