def get_circle_square(radius: float) -> float:
    result = 3.14 * radius**2
    return result

def get_rectangle_square(a: float, b:float = None) -> float:
    if b is None:
        b = a
    result = a * b
    return result

def test_get_rectangle_square():
    assert get_rectangle_square(10) == 100
    assert get_rectangle_square(10, 3) == 30
    assert get_rectangle_square(10, 0) == 0
    print("👍")
def test_get_circle_square():
    assert get_circle_square(5) == 78.5
    assert get_circle_square(0) == 0
    print("👍👍")
test_get_circle_square()
test_get_rectangle_square()