def gen_numbers(max_num):
    for i in range(max_num+1):
        yield i

numbers = gen_numbers(10)
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())