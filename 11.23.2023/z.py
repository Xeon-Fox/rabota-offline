hz_che=input("llas: ")
try:
    month_mesac_ai=int(hz_che)
except ValueError:
    print("число сделай")
else:
    match month_mesac_ai:
        case 1:
            print("джануари")
        case 2:
            print("фебруари")
        case 3:
            print("марч")
        case 4:
            print("эйприл")
        case 5:
            print("мэй")
        case 6:
            print("джун")
        case 7:
            print("джулай")
        case 8:
            print("оугуст")
        case 9:
            print("сэптэмбэр")
        case 10:
            print("октобэр")
        case 11:
            print("новэмбер")
        case 12:
            print("десэмбэр")
        case _:
            print("эт че")
