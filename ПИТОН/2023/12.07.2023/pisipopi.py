slovo_luboi_dlini=input("slovo luboi dlibi ")
polovina_plov=len(slovo_luboi_dlini) // 2
levo=slovo_luboi_dlini[:polovina_plov]
pravo=slovo_luboi_dlini[polovina_plov:]
print(levo, pravo)
levo = int(levo)
pravo = int(pravo)
summa=levo+pravo
print(summa)

