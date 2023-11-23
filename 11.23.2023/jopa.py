import math
# first_cool_number_nomer_cifra=input("1: ")
# second_cool_number_nomer_cifra=input("2: ")
# try:
#     first_cool_number_nomer_cifra = int(first_cool_number_nomer_cifra)
#     second_cool_number_nomer_cifra = int(second_cool_number_nomer_cifra)
# except ValueError:
#     print("че")
# else:
#     try:
#         proizvedene_chsla=first_cool_number_nomer_cifra/second_cool_number_nomer_cifra
#     except ZeroDivisionError:
#         print("0 нельзя але там вселенная всхлопница")
#     else:
#         print(proizvedene_chsla, " resultat korean chisla")

vvedeni_diamter_tak_nazivaemoi_okruzhnosti=input("помоги махмут найти радиус для донер кебаб лаваша. радиус: ")
try:
    vvedeni_diamter_tak_nazivaemoi_okruzhnosti=float(vvedeni_diamter_tak_nazivaemoi_okruzhnosti)
except ValueError:
    print("че это")
else:
    radius_doner_lavash=vvedeni_diamter_tak_nazivaemoi_okruzhnosti/2
    ploshad_lavash_lula_kebab=math.pi*radius_doner_lavash**2
    print(ploshad_lavash_lula_kebab)