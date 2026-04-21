def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? 4
         # What are the values of first and second at this point? 1
         # What happened? The words "Avoid" and "Such" were appended to the code
print()