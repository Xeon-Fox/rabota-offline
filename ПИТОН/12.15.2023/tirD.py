try:
    fd = open("txtforTIDR.txt", encoding='utf8')
except FileNotFoundError:
    print("нет")
    exit()
text=fd.read()
fd.close()

splitted_text=text.split("@")

print(splitted_text)
# before_at=splitted_text[0]
# after_at=splitted_text[1]
# if before_at == '':
#     print("нет")
# if after_at == '':
#     print("нет")
