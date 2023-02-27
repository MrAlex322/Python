from os import path

file_base = "base.txt"
all_data = []
id_record = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id_record

    with open(file_base, "r", encoding="utf-8") as f:

        all_data = [i.strip() for i in f]
        if all_data:
            id_record = int(all_data[-1][0])
        return all_data


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def add_new_records():
    global id_record
    list_info = ['surname', 'name', 'surname_2', 'phone_number']
    string = ''
    for i in list_info:
        string += input(f"Enter {i} ") + " "
    id_record += 1

    with open(file_base, "a", encoding="utf=8") as f:
        f.write(f'{id_record} {string}\n')


def search_records():
    search_items = exist_contact(0, input("Enter a search items: "))
    if search_items:
        print(*search_items, sep="\n")
    else:
        print("The data is not correct!")


def change_records(data_tuple):

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")


def delete_records():
    global all_data
    symbol = "\n"
    show_all()
    del_items = input("Enter the record id: ")

    if exist_contact(del_items, ""):
        all_data = [j for j in all_data if j[0] != del_items]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("Invalid entry!")


def exp_imp_records():
    pass


def exist_contact(id_2, data):

    if id_2:
        candidates = [i for i in all_data if id_2 in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def edit_menu():

    add_dict = {"1": "surname", "2": "name", "3": "surname_2", "4": "phone number"}

    show_all()
    record_id = input("Enter the record id: ")
    record_name = input("Enter the change: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. surname\n"
                           "2. name\n"
                           "3. patronymic\n"
                           "4. phone number\n"
                           "5. exit\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, record_name
                case "5":
                    return 0
                case _:
                    print("The data is not recognized, repeat the input.")
    else:
        print("The data is not correct!")



def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a records\n"
                       "3. Search a records\n"
                       "4. Change a records\n"
                       "5. Delete a records\n"
                       "6. Export a records\n"
                       "7. Import a records\n"
                       "8. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_records()
            case "3":
                search_records()
            case "4":
                work = edit_menu()
                if work:
                    change_records(work)
            case "5":
                delete_records()
            case "6":
                exp_bd()
            case"7":
                ipm_bd()
            case "8":
                play = False
            case _:
                print("Try again!")



def exp_bd():

    name = input("Enter the name of the file: ")
    symbol = "\n"

    if not path.exists(name):
        with open(f"{name}.txt", "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')


def ipm_bd():
    global file_base
    name = input("Enter the name of the file: ")
    if path.exists(name):
        file_base = name
        read_records()


main_menu()
