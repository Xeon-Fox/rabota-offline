database = []

def new_employee(full_name: str, birth_date, position, salary):
    if not full_name:
        return {"id": -1, "errorDesc": "Full Name not specified"}
    if not birth_date:
        return {"id": -1, "errorDesc": "Birth Date not specified"}
    if not position:
        return {"id": -1, "errorDesc": "Position not specified"}
    if salary <= 0:
        return {"id": -1, "errorDesc": "Salary not valid"}
    first_name, last_name = full_name.split(" ", 1)
    newcome = {
        "id": len(database),
        "firstName": first_name,
        "lastName": last_name,
        "birthDate": birth_date,
        "hiredDate": "yesterday",
        "firedDate": "",
        "position": position,
        "salary": salary
    }   
    database.append(newcome)
    return {"id": newcome["id"], "errorDesc": ""}

def fire_employee(id: int) -> dict:
    if not(0 <= id < len(database)):
     
        return {"id": -1, "errorDesc": "No such an employee exists"}
    if database[id]["fireDate"]:
        return {"id": -1, "errorDesc": "Employee is already fired"}
    database[id]["fireDate"] = "tommorow"
    return {"id": id, "errorDesc": ""}


def get_employee_id(full_name: str) -> int:
    try:
        first_name, last_name = full_name.split(" ", 1)
    except ValueError:
        return -1
    for man in database:
        if man["firstName"] + " " + ["lastName"] == full_name:
            return {"id": database["id"], "errorDesc": ""}
            

r1 = new_employee("Алексей Шевцов", "1488-05-01", "продавец говна", 184797)
r2 = new_employee("Игорь Линк", "1776-04-04", "Неподкупный обозреватель", 123121)
r3 = new_employee("Виктор Слидовский", "1984-04-02", "русофоб", 3)
r4 = new_employee("Lorem Ipsum", "0000-01-01", "черная дыра", 0)
r5 = new_employee("П П", "1981-04-12", "пистолет пулемет", 123)

id = get_employee_id("Алекесей Шевцов")
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)

print(database)