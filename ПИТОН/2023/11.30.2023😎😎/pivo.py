# import random;
# summa_gorod_v_ukraine=0
# aaaaaa_vvedi_chislo_aaaaa=1488
# while aaaaaa_vvedi_chislo_aaaaa!=0:
#     aaaaaa_vvedi_chislo_aaaaa=input("число введи есть же ")
#     try:
#         aaaaaa_vvedi_chislo_aaaaa=int(aaaaaa_vvedi_chislo_aaaaa)
#     except ValueError:
#         print("даун")
#         exit()
#     summa_gorod_v_ukraine+=aaaaaa_vvedi_chislo_aaaaa
# print(summa_gorod_v_ukraine)

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


# reshetechki_count=int(input("сока "))
# while reshetechki_count!=0:
#     print("#")
#     reshetechki_count-=1

# skoka_tam_nada=int(input("ж "))
# while skoka_tam_nada!=0:
#     print(skoka_tam_nada)
#     skoka_tam_nada-=1

# chislo_numba_van=int(input("ХАХАХАХАХАХ "))
# chislo_numba_too=int(input("АХАХАХАХ "))
# bsasd=0
# min_iz_nix_chislo = min(chislo_numba_van, chislo_numba_too)
# while bsasd<=min_iz_nix_chislo:
#     if bsasd%chislo_numba_van==0 and bsasd%chislo_numba_too==0:
#         print(bsasd)
#     bsasd+=1
        


# factoria_is_fancy=int(input("jkasdh "))
# sum_pum_fum=1
# while factoria_is_fancy >0:
#     sum_pum_fum=sum_pum_fum*factoria_is_fancy
#     factoria_is_fancy-=1
# print(sum_pum_fum)

# while True:
#     reshai_tvar=int(input("РЕШИ ЭТО БЬЫСТРО "))
#     if reshai_tvar==6:
#         print("красава")
#         break

# tisaicha=1000
# countttt=0
# while True:
#     tisaicha=tisaicha/2
#     if tisaicha<50:
#         break
#     print(tisaicha)
#     countttt+=1
# print(countttt,"дэлэний")

rowseki=8
kolonni=8
r=0
while r< rowseki:
    r +=1
    current_stuff=0
    while current_stuff < kolonni:
        current_stuff+=1
        if current_stuff%2==0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print("#")
