hz_che=input("llas: ")
message_whatsapp_viber_Skype=""
match hz_che:
    case "понедельник":
        message_whatsapp_viber_Skype="Понедельник-день-бездельник"
    case "вторник":
        message_whatsapp_viber_Skype="12-день-бездельник"
    case "среда":
        message_whatsapp_viber_Skype="1212-день-бездельник"
    case "четверг":
        message_whatsapp_viber_Skype="Понедель1112ник-день-бездельник"
    case "пятница":
        message_whatsapp_viber_Skype="Понедель12122112ник-день-бездельник"
    case "суббота":
        message_whatsapp_viber_Skype="Понеде1121212льник-день-бездельник"
    case "воскресенье":
        message_whatsapp_viber_Skype="Понедел12122112ьник-день-бездельник"
    case _:
        amessage_whatsapp_viber_Skype="эт че"
print(message_whatsapp_viber_Skype)