def test_get_names():
    assert get_names([3,5,1]) == ["три", "пять", "один"]
    assert get_names((4, 0)) == ["четыре", "ноль"]
    assert get_names([]) == []
    assert get_names((5, 13)) == ["пять", ""]
    assert get_names(1,2,3) == ["один", "два", "три"]
    print("👍")

def get_names(arg, *args) -> list:
    if arg == list or tuple:
        result = []
        for number in arg:
            match number:
                case 0:
                    result.append("ноль")
                case 1:
                    result.append("один")
                case 2:
                    result.append("два")
                case 3:
                    result.append("три")
                case 4:
                    result.append("четыре")
                case 5:
                    result.append("пять")
                case 6:
                    result.append("шесть")
                case 7:
                    result.append("семь")
                case 8:
                    result.append("восемь")
                case 9:
                    result.append("девять")
                case _:
                    result.append("")
        return result
    if arg == int:
        result = []
        for number in args:
            match number:
                case 0:
                    result.append("ноль")
                case 1:
                    result.append("один")
                case 2:
                    result.append("два")
                case 3:
                    result.append("три")
                case 4:
                    result.append("четыре")
                case 5:
                    result.append("пять")
                case 6:
                    result.append("шесть")
                case 7:
                    result.append("семь")
                case 8:
                    result.append("восемь")
                case 9:
                    result.append("девять")
                case _:
                    result.append("")
        return result
        

test_get_names()
    

def get_names2(*array) -> list:
    result = []
    for number in array:
        match number:
            case 0:
                result.append("ноль")
            case 1:
                result.append("один")
            case 2:
                result.append("два")
            case 3:
                result.append("три")
            case 4:
                result.append("четыре")
            case 5:
                result.append("пять")
            case 6:
                result.append("шесть")
            case 7:
                result.append("семь")
            case 8:
                result.append("восемь")
            case 9:
                result.append("девять")
            case _:
                result.append("")
    return result