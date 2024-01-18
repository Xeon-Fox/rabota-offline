array = ["Томирис", "Семён", "Аджибала", "Абулхаир", "Имангали", "Эрик", "Абулхаир", "Алмас", "Виталий", "Аян"]

first_letters = map(lambda x: x[0], array)

print(tuple(first_letters))

lenghts = map(len, array)
print(list(lenghts))

user_in = "6, 33, 4, 8, 19"
numbers = map(int, user_in.split(", "))
squares = map(lambda x: x**2, numbers)

reverse = map(lambda x: x[::-1], array)
print(list(reverse))

roots = map(lambda x: x**0.5, range(1, 11))
print(tuple(roots))