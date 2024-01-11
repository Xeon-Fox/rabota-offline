try:
    fd = open("input.txt", encoding='utf8')
except FileNotFoundError:
    print("нет")
    exit()
text=fd.read()
fd.close()

slovo_iznachalnoe=input("изначальное слвоо заменить которое да ")
zamenat_slovo=input("заменаемое слово ")

new_text=text.replace(slovo_iznachalnoe.upper(), zamenat_slovo.upper())
new_text2=new_text.replace(slovo_iznachalnoe.lower(), zamenat_slovo.lower())
new_text3=new_text2.replace(slovo_iznachalnoe.capitalize(), zamenat_slovo.capitalize())

print(new_text3)