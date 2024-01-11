listovka=[3, 9, 8, 4, 5, 1]
for i in range(len(listovka)-1):
    first=listovka[i]
    second=listovka[i+1]
    if first > second:
        print(listovka[i])
    