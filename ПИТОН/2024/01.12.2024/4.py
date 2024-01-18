from functools import reduce

array = ["Томирис", "Семён", "Аджибала", "Абулхаир", "Имангали", "Эрик", "Абулхаир", "Алмас", "Виталий", "Аян", "Семён"]
numbers = (87, -4, -86, 75, 98, 6, 4, 87, -4, 658, -98)

sum = reduce(lambda acc, x: acc+x, numbers)
print(sum)

names = reduce(lambda acc, x: acc + ", " + x, array)
print(names)

names = reduce(lambda acc, x: acc + ", " + x, array)
print(names)

names2 = reduce(lambda acc, x: acc + 1 if x[0]=="А" else acc, array, 0)
print(names2)

def name_counter(acc, name):
    if name in acc:
        acc[name] += 1
    else:
        acc[name] = 1
    return acc

counts = reduce(name_counter, array, {})
print(counts)

first_names = reduce(lambda acc, x: acc + x[0], array, "")
print(first_names)