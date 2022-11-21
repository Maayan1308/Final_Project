# Check Id validation #
def check_id(emp_id):
    id_check1 = []
    i = 0
    for x in str(emp_id):
        if i % 2 == 0:
            id_check1.append(int(x))
        else:
            id_check1.append(int(x) * 2)
        i += 1
    id_check2 = []
    i = 0
    for x in id_check1:
        if x > 9:
            id_check2.append(1 + x % 10)
        else:
            id_check2.append(int(x))
        i += 1
    final_check_id = 0
    for x in id_check2:
        final_check_id += x
    return final_check_id


# Check if Employee exist in DB #
def check_if_employee_exist(emp_id):
    with open('employees_DB.txt', 'r') as f1:
        if emp_id in f1.read():
            return True
        else:
            return False


def add_new_employee_manually():
    row = []
    id_flag = True
    last_name_flag = True
    first_name_flag = True
    phone_flag = True
    age_flag = True
    # Check ID and if Employee already exist #
    while id_flag:
        emp_id = input("Please Enter Employee ID:")
        # check if ID contains digits only #
        if not all(char.isdigit() for char in emp_id):
            print("Oops! Employee ID should contains Digits only")
            continue
        # check ID len = 9
        if len(emp_id) != 9:
            print("Oops! Please enter 9 digits Employee ID")
            continue
        # check ID validation algorithm #
        final_check_id = check_id(emp_id)
        if final_check_id % 10 != 0:
            print("Invalid ID number, please try again")
            continue
        if check_if_employee_exist(emp_id):
            print("Employee Already Exist in DB")
            continue
        row.append(emp_id)
        id_flag = False
    # Check Last Name #
    while last_name_flag:
        emp_last_name: str = input("Please Enter Employee Last Name:")
        if not all(char.isalpha() for char in emp_last_name):
            print("Oops! Employee Last Name should contains letters only")
            continue
        else:
            row.append(emp_last_name)
            last_name_flag = False
    # Check First Name #
    while first_name_flag:
        emp_first_name: str = input("Please Enter Employee First Name:")
        if not all(char.isalpha() for char in emp_first_name):
            print("Oops! Employee First Name should contains letters only")
            continue
        else:
            row.append(emp_first_name)
            first_name_flag = False
    # Check Phone Number #
    while phone_flag:
        phone_num = input("Please Enter Employee Phone Number (digits only, without space):")
        if len(phone_num) != 10:
            print("Oops! Employee Phone Number should contains 10 Digits Number")
            continue
        if not all(char.isdigit() for char in phone_num):
            print("Oops! Employee Phone Number should contains Digits only")
            continue
        else:
            row.append(phone_num)
            phone_flag = False
    while age_flag:
        try:
            age = int(input("Please Enter Employee Age:"))
        except ValueError:
            print("Oops! Employee age should be number")
            continue
        if age < 16 or age > 70:
            print("Oops! Employee age should be number between 16-70")
            continue
        else:
            row.append(age)
            age_flag = False
    print("Employees was successfully added")
    return row


def delete_employee_manually():
    import csv
    row = []
    id_flag = True
    while id_flag:
        emp_id = input("Please Enter Employee ID you would like to Delete:")
        # check if ID contains digits only #
        if not all(char.isdigit() for char in emp_id):
            print("Oops! Employee ID should contains Digits only")
            continue
        # check ID len = 9
        if len(emp_id) != 9:
            print("Oops! Please enter 9 digits Employee ID")
            continue
        if check_if_employee_exist(emp_id):
            with open('employees_DB.txt', 'r') as f1:
                reader = csv.reader(f1)
                index = 0
                for row in reader:
                    if len(row) > 0:
                        if row[0] == emp_id:
                            return row
                            break
                        else:
                            index += 1
                    else:
                        index += 1
            id_flag = False
        else:
            print("Employee Don't exist in DB")
            continue


def main():
    import csv
    header = ['Employee ID', 'Last Name', 'First Name', 'Phone', 'Age']
    with open('employees_DB.txt', 'w') as f1:
        writer = csv.writer(f1)
        writer.writerow(header)

    flag = True
    while flag:
        try:
            num = int(input("""Please choose what you would like to do:
        1)  Add New Employee manually
        2)	Add New Employee from a file
        3)	Delete Employee manually
        4)	Delete Employee from a file
        5)	Mark Attendance
        6)	Generate Attendance report of an Employee
        7)	Generate Attendance Current Month report
        8)	Generate Attendance late report
        9)	Exit 
        """))
        except ValueError:
            print("Oops! Please choose number between 1-9")
            continue
        if num < 1 or num > 9:
            print("Invalid options, please try again")
        elif num == 1:
            row = add_new_employee_manually()
            with open('employees_DB.txt', 'a') as f1:
                writer = csv.writer(f1)
                writer.writerow(row)
        elif num == 2:
            print("2")
        elif num == 3:
            row = delete_employee_manually()
            with open('employees_DB.txt', 'w') as f1:
                writer = csv.writer(f1)
                writer.drop(row)
            print("Employees was successfully Deleted")
        elif num == 4:
            print("4")
        elif num == 5:
            print("5")
        elif num == 6:
            print("6")
        elif num == 7:
            print("7")
        elif num == 8:
            print("8")
        elif num == 9:
            flag = False
            print("Goodbye")


if __name__ == "__main__":
    main()
