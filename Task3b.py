def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, when will a call to this function evaluate this statement? if a is greater than b and c
    elif b > c:
        return b + c             # In general, when will a call to this function evaluate this statement? if b is greater an c
    else:
        return 2 * c             # In general, when will a call to this function evaluate this statement? if none of the above are true


answer1 = function2(3, 2, 1)     # What is the value of answer1? 1
answer2 = function2(2, 3, 1)     # What is the value of answer2? 4
answer3 = function2(2, 1, 3)     # What is the value of answer3? 6
print()