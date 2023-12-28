def hexxed(numbers=[]) -> list:
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result

def test_the_hexx():
    assert hexxed([1,2,3,4]) == [2,4]
    assert hexxed([1,3,5,7,11,13,17]) == []
    assert hexxed([]) == []
    assert hexxed((1,2,7,4,8)) == [2, 4, 8]
    assert hexxed() == []
    print("я под метамфитамином")
test_the_hexx()