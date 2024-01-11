def is_same_type(array) -> bool:
    if not array:
        return False
    for i in array:
        if type(i) != type(array[0]):
            return False
    return True

def test():
    assert is_same_type((1, "yes", False)) == False
    assert is_same_type((1, 2, 3)) == True
    assert is_same_type([8]) == True
    assert is_same_type([8, 4, 9, "hui", 2]) == False
    assert is_same_type(({"Name": "Benito"},{},{})) == True
    assert is_same_type(["Adolf", 4]) == False  
    assert is_same_type([]) == False
    print("я на солях")

test()