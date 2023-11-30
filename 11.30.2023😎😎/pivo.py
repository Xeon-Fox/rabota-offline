# import random;
summa_gorod_v_ukraine=0
aaaaaa_vvedi_chislo_aaaaa=1488
while aaaaaa_vvedi_chislo_aaaaa!=0:
    aaaaaa_vvedi_chislo_aaaaa=input("число введи есть же ")
    try:
        aaaaaa_vvedi_chislo_aaaaa=int(aaaaaa_vvedi_chislo_aaaaa)
    except ValueError:
        print("даун")
        exit()
    summa_gorod_v_ukraine+=aaaaaa_vvedi_chislo_aaaaa
print(summa_gorod_v_ukraine)

# numeracia_uraaa=1
# while numeracia_uraaa<11:
#     cheto_tam=numeracia_uraaa**2
#     numeracia_uraaa+=1
#     print(cheto_tam)

# while True:
#     peremennai_random=random.randint(1,10)
#     print(peremennai_random)
#     if peremennai_random==7:
#         print("все")
#         break