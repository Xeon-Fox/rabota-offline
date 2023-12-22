iskomi_simvol=input("🤔🤔🤔 ")
celevaia_stroka=input("🤞🤞🤞 ")
first=-1
last=-1
curremt_bukva=""
for i in range(len(celevaia_stroka)):
    curremt_bukva=celevaia_stroka[i]
    if curremt_bukva==iskomi_simvol:
        first=i
        break
for i in range(len(celevaia_stroka)):
    curremt_bukva=celevaia_stroka[i]
    if curremt_bukva==iskomi_simvol:
        last=i
result=[first, last]
print(result)
    