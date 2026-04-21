def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated? both of them since n is never less than m
    else:
        return m

first = smallest(3, 2)       # What is the value of first? value of first 29
second = smallest(2, 2)      # What is the value of second? Is this a reasonable result? Why or why not? 29. Yes because n is also less than m
print()