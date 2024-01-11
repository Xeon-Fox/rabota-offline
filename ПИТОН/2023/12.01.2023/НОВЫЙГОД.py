# kratos=int(input("asd "))
# for i in range(1,100):
#     if i % kratos == 0:
#         print(i)

# ot_skolki=int(input("asd "))
# do_skolki=int(input("ASdasd "))
# cooonter=1
# for i in range(ot_skolki, do_skolki):
#     if i % 4 == 0:
#         print(i)
#         cooonter=0
#     cooonter+=1

# chislo_vvedi_chel=int(input("ASdasd "))
# how_many_times_it_podelilos=0
# for i in range(1,chislo_vvedi_chel):
#     if chislo_vvedi_chel % i == 0:
#         how_many_times_it_podelilos+=1
#     if how_many_times_it_podelilos >= 2:
#         print("не простое")
#         break
#     i+=1
# if how_many_times_it_podelilos == 1:
#     print("простое")

# chislo_numba_van=int(input("АХАХАХАХ "))
# for i in range(1,chislo_numba_van+1):
#     if chislo_numba_van%i==0:
#         print(i)

# N_chislo_krutoe=int(input("asd "))
# current_Chislo_kotoroe_shas=1
# before_that_thing=1
# poslednee_kotoroe_nam_nada=0
# for i in range(N_chislo_krutoe):
#     poslednee_kotoroe_nam_nada=before_that_thing
#     before_that_thing=current_Chislo_kotoroe_shas
#     current_Chislo_kotoroe_shas=before_that_thing+poslednee_kotoroe_nam_nada
#     print(current_Chislo_kotoroe_shas)

# while True:
#     vvod_inputer_computer=int(input("pervoi vvedi "))
#     second_vvod_computer_inputer=int(input("jest "))
#     znak_che_tam_nado_sdelat=input("Asdasd ")
#     match znak_che_tam_nado_sdelat:
#         case "+":
#             result = vvod_inputer_computer+second_vvod_computer_inputer
#             print(result)
#         case "-":
#             result = vvod_inputer_computer-second_vvod_computer_inputer
#             print(result)
#         case "*":
#             result = vvod_inputer_computer*second_vvod_computer_inputer
#             print(result)
#         case "/":
#             result = vvod_inputer_computer/second_vvod_computer_inputer
#             print(result)
#         case _:
#             print("че")
#     eshe_budesh=input("еще будешь ")
#     if eshe_budesh == "да":
#         continue
#     else:
#         break

inputer=int(input('sda '))
kolvo_chisel=len(inputer)
for i in inputer:
    second_number=first_number
    first_number=i