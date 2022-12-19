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
    import csv
    with open('employees_DB.csv', 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row[0] == emp_id:
                return True
        else:
            return False


# Employee ID Checks
def employee_id_checks(emp_id):
    id_flag = True
    while id_flag:
        # check if ID contains digits only #
        if not all(char.isdigit() for char in emp_id):
            print("Oops! Employee ID should contains Digits only")
            return False
        # check ID len = 9
        if len(emp_id) != 9:
            print("Oops! Please enter 9 digits Employee ID")
            return False
        # check ID validation algorithm #
        final_check_id = check_id(emp_id)
        if final_check_id % 10 != 0:
            print("Invalid ID number, please check ID")
            return False
        id_flag = False
    return True


def employee_last_name_check(emp_last_name):
    last_name_flag = True
    while last_name_flag:
        if not all(char.isalpha() for char in emp_last_name):
            print("Oops! Employee Last Name should contains letters only")
            return False
        else:
            last_name_flag = False
    return True


def employee_first_name_check(emp_first_name):
    first_name_flag = True
    while first_name_flag:
        if not all(char.isalpha() for char in emp_first_name):
            print("Oops! Employee Last Name should contains letters only")
            return False
        else:
            first_name_flag = False
    return True


def employee_phone_number_check(phone_num):
    phone_flag = True
    while phone_flag:
        if len(phone_num) != 10:
            print("Oops! Employee Phone Number should contains 10 Digits Number")
            return False
        if not all(char.isdigit() for char in phone_num):
            print("Oops! Employee Phone Number should contains Digits only")
            return False
        else:
            phone_flag = False
    return True


def employee_age_check(age):
    age_flag = True
    while age_flag:
        if not all(char.isdigit() for char in age):
            print("Oops! Employee age should be number")
            return False
        if int(age) < 16 or int(age) > 70:
            print("Oops! Employee age should be number between 16-70")
            return False
        else:
            age_flag = False
    return True


def add_new_employee_manually():
    row = []
    # Check ID and if Employee already exist #
    emp_id = input("Please Enter Employee ID:")
    while not employee_id_checks(emp_id):
        emp_id = input("Please Enter Employee ID:")
    if check_if_employee_exist(emp_id):
        print("Employee Already Exist in DB")
    else:
        row.append(emp_id)
    # Check Last Name #
    emp_last_name = input("Please Enter Employee Last Name:")
    while not employee_last_name_check(emp_last_name):
        emp_last_name = input("Please Enter Employee Last Name:")
    row.append(emp_last_name)
    # Check First Name #
    emp_first_name = input("Please Enter Employee First Name:")
    while not employee_first_name_check(emp_first_name):
        emp_first_name = input("Please Enter Employee First Name:")
    row.append(emp_first_name)
    # Check Phone Number #
    phone_num = input("Please Enter Employee Phone Number (digits only, without space):")
    while not employee_phone_number_check(phone_num):
        phone_num = input("Please Enter Employee Phone Number (digits only, without space):")
    row.append(phone_num)
    # Check Employee Age
    age = input("Please Enter Employee Age:")
    while not employee_age_check(age):
        age = input("Please Enter Employee Age:")
    row.append(age)
    return row


def add_employees_from_file(file_path):
    import csv
    import os
    header = ['Employee ID', 'Last Name', 'First Name', 'Phone', 'Age']
    with open(os.path.abspath(file_path), 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row == header:
                continue
            else:
                if not employee_id_checks(row[0]):
                    print("Invalid ID Number for Employee " + row[0] + " was not added")
                    continue
                if check_if_employee_exist(row[0]):
                    print("Employee " + row[0] + " Already Exist in DB, Employee was not added")
                    continue
                if not employee_last_name_check(row[1]):
                    print("Invalid Last Name for Employee-" + row[0] + ", Employees was not added")
                    continue
                if not employee_first_name_check(row[2]):
                    print("Invalid First Name for Employee-" + row[0] + ", Employees was not added")
                    continue
                if not employee_phone_number_check(row[3]):
                    print("Invalid Phone Number for Employee-" + row[0] + ", Employees was not added")
                    continue
                if not employee_age_check(row[4]):
                    print("Invalid Age for Employee-" + row[0] + ", Employees was not added")
                    continue
            with open('employees_DB.csv', 'a', newline='') as f2:
                writer = csv.writer(f2)
                writer.writerow(row)
            print("Employee " + row[0] + " was successfully added")


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
            lines = list()
            with open('employees_DB.csv', 'r') as f1:
                reader = csv.reader(f1)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == emp_id:
                            lines.remove(row)
            with open('employees_DB.csv', 'w', newline='') as f1:
                writer = csv.writer(f1)
                writer.writerows(lines)
            print("Employee was successfully deleted")
            id_flag = False
        else:
            print("Employee Don't exist in DB")
            continue


def delete_employees_from_file(file_path):
    import csv
    import os
    header = ['Employee ID','Last Name','First Name','Phone','Age']
    with open(os.path.abspath(file_path), 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row == header:
                continue
            else:
                if not all(char.isdigit() for char in row[0]):
                    print("Oops! Employee ID should contains Digits only, Employee" + row[0] + "was not deleted")
                    continue
                # check ID len = 9
                if len(row[0]) != 9:
                    print("Oops! Please enter 9 digits Employee ID, Employee" + row[0] + "was not deleted")
                    continue
                if check_if_employee_exist(row[0]):
                    lines = list()
                    with open('employees_DB.csv', 'r') as f2:
                        reader = csv.reader(f2)
                        for rows_to_keep in reader:
                            lines.append(rows_to_keep)
                            for field in rows_to_keep:
                                if field == row[0]:
                                    lines.remove(rows_to_keep)
                    with open('employees_DB.csv', 'w', newline='') as f2:
                        writer = csv.writer(f2)
                        writer.writerows(lines)
                    print("Employee " + row[0] + " was successfully deleted")


def find_employee_last_name(emp_id):
    import csv
    with open('employees_DB.csv', 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row[0] == emp_id:
                return row[1]


def find_employee_first_name(emp_id):
    import csv
    with open('employees_DB.csv', 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row[0] == emp_id:
                return row[2]


def create_employee_attendance_report(emp_id):
    import csv
    header = ['Employee ID', 'Last Name', 'First Name', 'Date', 'Attendance']
    lines = list()
    lines.append(header)
    with open('employees_Attendance.csv', 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row == header:
                continue
            else:
                if row[0] == emp_id:
                    lines.append(row)
    with open('employee_' + emp_id + '_attendance_report.csv', 'w', newline='') as f2:
        writer = csv.writer(f2)
        writer.writerows(lines)
    print("Attendance Report for employee " + emp_id + " was successfully created")


def create_month_attendance_report():
    import csv
    import datetime
    header = ['Employee ID', 'Last Name', 'First Name', 'Date', 'Attendance']
    lines = list()
    lines.append(header)
    with open('employees_Attendance.csv', 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row == header:
                continue
            else:
                attendance_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                if attendance_date.month == datetime.date.today().month:
                    lines.append(row)
    with open('employee_' + str(datetime.date.today().strftime('%Y-%m')) + '_attendance_report.csv', 'w', newline='') \
            as f2:
        writer = csv.writer(f2)
        writer.writerows(lines)
    print("Attendance Monthly Report was successfully created")


def create_attendance_late_report():
    import csv
    import datetime
    header = ['Employee ID', 'Last Name', 'First Name', 'Date', 'Attendance']
    lines = list()
    lines.append(header)
    late_time = datetime.datetime.strptime('2022-12-19 09:30:00', '%Y-%m-%d %H:%M:%S')
    with open('employees_Attendance.csv', 'r') as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row == header:
                continue
            else:
                attendance_date = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                print(attendance_date.time())
                print(late_time.time())
                if attendance_date.time() >= late_time.time():
                    lines.append(row)
    with open('attendance_late_report.csv', 'w', newline='') \
            as f2:
        writer = csv.writer(f2)
        writer.writerows(lines)
    print("Attendance Late Report was successfully created")


def main():
    import csv
    import os
    import datetime
    header1 = ['Employee ID', 'Last Name', 'First Name', 'Phone', 'Age']
    with open('employees_DB.csv', 'w', newline='') as f1:
        writer = csv.writer(f1)
        writer.writerow(header1)
    header2 = ['Employee ID', 'Last Name', 'First Name', 'Date', 'Attendance']
    with open('employees_Attendance.csv', 'w', newline='') as f2:
        writer = csv.writer(f2)
        writer.writerow(header2)
    flag = True
    while flag:
        try:
            num = int(input("""Please choose what you would like to do:
        1)  Add New Employee manually
        2)	Add New Employees from a file
        3)	Delete Employee manually
        4)	Delete Employees from a file
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
            print("Invalid option, please try again")
        elif num == 1:
            row = add_new_employee_manually()
            with open('employees_DB.csv', 'a', newline='') as f1:
                writer = csv.writer(f1)
                writer.writerow(row)
            print("Employees was successfully added")
        elif num == 2:
            file_path = input("please enter file path:")
            while not os.path.exists(file_path):
                print("Oops! invalid file path")
                file_path = input("please enter file path:")
            add_employees_from_file(file_path)
        elif num == 3:
            delete_employee_manually()
        elif num == 4:
            file_path = input("please enter file path:")
            while not os.path.exists(file_path):
                print("Oops! invalid file path")
                file_path = input("please enter file path:")
            delete_employees_from_file(file_path)
        elif num == 5:
            emp_id = input("Please Enter Employee ID:")
            while not check_if_employee_exist(emp_id):
                print("Employee Does not exist in DB")
                emp_id = input("Please Enter Employee ID:")
            else:
                row = [emp_id, find_employee_last_name(emp_id), find_employee_first_name(emp_id),
                       datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'), "V"]
                with open('employees_Attendance.csv', 'a', newline='') as f2:
                    writer = csv.writer(f2)
                    writer.writerow(row)
                print("Employee Attendance was marked")
        elif num == 6:
            emp_id = input("Please Enter Employee ID:")
            while not check_if_employee_exist(emp_id):
                print("Employee Does not exist in DB")
                emp_id = input("Please Enter Employee ID:")
            else:
                create_employee_attendance_report(emp_id)
        elif num == 7:
            create_month_attendance_report()
        elif num == 8:
            create_attendance_late_report()
        elif num == 9:
            flag = False
            print("Goodbye")


if __name__ == "__main__":
    main()
