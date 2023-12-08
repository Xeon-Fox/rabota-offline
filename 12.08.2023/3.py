spisok1 = [1, 2, 4, 3, 5, 7]
spisok2 = [2, 6, 4, 7, 5, 1]
i=0
while i < len(spisok1):
    for k in range(len(spisok2)-1):
        if spisok1[i] == spisok2[k]:
            spisok1.pop(i)     
    i+=1
print(spisok1)