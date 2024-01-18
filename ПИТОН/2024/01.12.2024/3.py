array = ["Томирис", "Семён", "Аджибала", "Абулхаир", "Имангали", "Эрик", "Абулхаир", "Алмас", "Виталий", "Аян"]

longest = filter(lambda x: x[0] > "Н", array)
print(list(longest))

numbers = (87, -4, -86, 75, 98, 6, 4, 87, -4, 658, -98)
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))