import mysql.connector
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="!Ilovechewy123" #PASSWORD SHOULD BE WHATEVER FOR YOUR LOCAL MACHINE
)

def initDB():
    mycursor = mydb.cursor()
    mycursor.execute('USE thefinaldb') #thefinaldb should be changed to whatever your local db is called

def displayMainMenu():
    print("------------MENU------------")
    print("0. exit")
    print("1. Patient")
    print("2. Empolyee")
    print("3. Department")
    print("4. Surgery")
    print("5. Assign Doctor to Surgery") #Conduct
    print("6. Assign Surgery to Patient") #Undergoes
    print("7. Assign Nurse to Doctor") #Works_For
    print("8. Assign Doctor to Patient") #Treats
    print("9. Mark a Surgery as Complete") #Surgery Complete
    print("10. Aggregate Functions")
    print("----------------------------")

def displayPatientMenu():
    print("-----------PATIENT----------")
    print("0. exit")
    print("1. Add")#
    print("2. Modify")#
    print("3. Discharge")#
    print("4. Show All")#
    print("----------------------------")

def displayEmployeeMenu():
    print("---------EMPLOYEE----------")
    print("0. exit")
    print("1. Hire Employee")#
    print("2. Fire Employee")#
    print("3. Modify Employee")#
    print("4. Reassign Nurse")#
    print("5. Show All Doctors")#
    print("6. Show All Nurses")#
    print("----------------------------")

def displayDepartmentMenu():
    print("------------DEPT------------")
    print("0. exit")
    print("1. Add")#
    print("2. Modify")#
    print("3. Delete")#
    print("4. Show All")#
    print("----------------------------")

def displaySurgeryMenu():
    print("-----------SURGERY----------")
    print("0. exit")
    print("1. Show All")#
    print("----------------------------")

def displayAgFuncMenu():
    print("-----AGGREGATE FUNCTIONS-----")
    print("0. exit")
    print("1. Average Mortality Rate Across Surgeries")#
    print("2. Average Cost of All Surgeries")#
    print("3. Find Max Budget")#
    print("----------------------------")

def exit():
    n = input("Press Enter to continue: ")
    os.system('cls')
    run()


#------PATIENT QUERIES------
def addPatient():
    mycursor = mydb.cursor()
    print("--Enter Patient information--")
    #patientID = int(input("Enter the Patient ID: "))
    name = input("Enter the Patient's name: ")
    age = int(input("Enter the Patient's age: "))
    gender = input("Enter the Patient's gender (M/F): ")
    healthInsurance = bool(input("Enter the status of the Patient's health insurance (1 for Y/0 for N): "))
    pec = input("Enter any Pre-Existing Conditions: ")

    sql = 'INSERT INTO `patient` (`NAME`,`AGE`, `GENDER`, `HEALTH_INSURANCE`, `PREEXIST_COND`) VALUE (%s,%s,%s,%s,%s)'
    val = (name, age, gender, healthInsurance, pec)
    mycursor.execute(sql, val)
    mydb.commit()

    print("--SUCCESS--")
    exit()

def modify_patient():
    mycursor = mydb.cursor()
    patientID = int(input("Enter Patient ID for modifications: "))
    patientName = input("Enter Previous or new Patient name: ")
    patientAge = int(input("Enter Previous or new Patient age: "))
    patientGender = input("Enter Previous or new Patient gender: ")
    patientHealthInsur = bool(input("Enter if Patient has Health Insurance(0 for N/1 for Y): "))
    patientPreExistCond = input("Enter New or old Pre-Existing Conditions: ")

    #(SELECT * FROM Patient WHERE PATIENTID=`patientID`)
    sql = 'UPDATE `patient` SET name=%s, age=%s, gender=%s, HEALTH_INSURANCE=%s, PREEXIST_COND=%s WHERE id=%s'
    val = (patientName, patientAge, patientGender, patientHealthInsur, patientPreExistCond, patientID)
    mycursor.execute(sql,val)
    mydb.commit()

    print("--Modification Complete--")
    exit()

def dischargePatient():
    mycursor = mydb.cursor()
    patientID = int(input("Enter the ID of the patient that is to be discharged: "))
    #sql = 'UPDATE `patient` SET name=%s, age=%s, gender=%s, HEALTH_INSURANCE=%s, PREEXIST_COND=%s WHERE id=%s'
    sql = 'DELETE FROM `patient` WHERE id=%s' % (patientID)
    mycursor.execute(sql)
    mydb.commit()
    print("--SUCCESS--")
    exit()

def showPatients():
    mycursor = mydb.cursor()
    print("--All Patients--\n")
    mycursor.execute('SELECT * FROM patient')
    patientList = mycursor.fetchall()
    for p in patientList:
        print("--Patient", p[0], "--")
        print("Name:", p[1])
        print("Age:", p[2])
        print("Gender:", p[3])
        print("Health Insurance Status:", p[4])
        print("Pre-Existing Condition:", p[5])
        print("\n")
    print("All Patients listed")
    exit()


#------EMPLOYEE QUERIES------
def hire_employee():
    mycursor = mydb.cursor()
    display_employee_menu()
    n = int(input("Insert option:"))

    if n == 1:
        os.system("cls")
        Name = input('Enter Nurse name : ')
        Did = input('Enter user Doctor ID : ')

        #sql in here too
        #come back and check if Doctor id's exist
        sql = 'INSERT INTO `Nurse` (`Name`,`Did`) VALUES (%s, %s)'
        val = (Name, Did)
        mycursor.execute(sql,val)
        mydb.commit()

        print('------ SUCCESS ------\n')
        exit()
    elif n == 2:
        os.system("cls")
        name = input('Enter Doctor name : ')
        specialization = input('Enter user Doctor specialization : ')

        #sql goes heresql = 'INSERT INTO `Nurse` (`Name`,`Did`) VALUES (%s, %i)'
        sql = 'INSERT INTO `Doctor` (`name`,`specialization`) VALUES (%s, %s)'
        val = (name, specialization)
        mycursor.execute(sql,val)
        mydb.commit()

        print('------ SUCCESS ------\n')
        exit()
    elif n == 3:
        os.system("cls")
        #go back
        exit()
    else:
        os.system("cls")
        hire_employee()
def display_employee_menu():
    print('------ Hire Employee ------\n')
    print('1. Nurse\n')
    print('2. Doctor\n')
    print('3. Back\n')
    return

def fire_employee():
    mycursor = mydb.cursor()
    display_femployee_menu()
    n = int(input("Insert option:"))

    if n == 1:
        os.system("cls")
        NurseID = input('Enter Nurse ID : ')

        #sql in here too
        #come back and check if Doctor id's exist
        sql = 'DELETE FROM `Nurse` WHERE nid=%s' % (NurseID)
        mycursor.execute(sql)
        mydb.commit()

        print('------ SUCCESS ------\n')
        exit()
    elif n == 2:
        os.system("cls")
        DoctorID = int(input("Enter Doctor ID : "))


        #sql goes heresql = 'INSERT INTO `Nurse` (`Name`,`Did`) VALUES (%s, %i)'
        sql = 'DELETE FROM `Doctor` WHERE id=%s' % (DoctorID)
        mycursor.execute(sql)
        mydb.commit()

        print('------ SUCCESS ------\n')
        exit()
    elif n == 3:
        os.system("cls")
        #go back
        exit()
    else:
        os.system("cls")
        hire_employee()
def display_femployee_menu():
    print('------ Fire Employee ------\n')
    print('1. Nurse\n')
    print('2. Doctor\n')
    print('3. Back\n')
    return

def modify_employee():
    mycursor = mydb.cursor()

    choice = int(input("Modify Doctor(0) or Modify Nurse(1): "))
    if choice == 0:
        docID = int(input("Enter Doctor ID for modifications: "))
        docName = input("Enter Previous or new Doctor name: ")
        docSpec = input("Enter Previous or new Doctor Specialization: ")

        sql = 'UPDATE doctor SET name=%s, specialization=%s WHERE id=%s'
        val = (docName, docSpec, docID)
        mycursor.execute(sql,val)
        mydb.commit()

        print("--Doctor Modification Complete--")
        exit()
    elif choice == 1:
        nurseID = int(input("Enter Doctor ID for modifications: "))
        nurseName = input("Enter Previous or new Nurse name: ")

        sql = 'UPDATE nurse SET name=%s WHERE id=%s'
        val = (nurseName, nurseID)
        mycursor.execute(sql,val)
        mydb.commit()

        print("--Nurse Modification Complete--")
        exit()

def reassign_nurse():
    mycursor = mydb.cursor()
    print('------ Reassign Nurse ------\n')
    NID = input('Enter Nurse ID : ')
    DID = input('Enter New Doctor ID: ')

    sql = 'UPDATE Nurse SET Did = %s WHERE NID=%s'
    val = (DID, NID)
    mycursor.execute(sql,val)
    mydb.commit()

    print('------ SUCCESS ------\n')
    exit()

def showDoctors():
    mycursor = mydb.cursor()
    print("--All Doctors--\n")
    mycursor.execute('SELECT * FROM doctor')
    doctorList = mycursor.fetchall()
    for d in doctorList:
        print("--Doctor", d[0], "--")
        print("Name:", d[1])
        print("Specialization:", d[2])
        print("\n")
    print("All Doctors listed")
    exit()

def showNurses():
    mycursor = mydb.cursor()
    print("--All Nurses--\n")
    mycursor.execute('SELECT * FROM nurse')
    nurseList = mycursor.fetchall()
    for n in nurseList:
        print("--Nurse", n[0], "--")
        print("Name:", n[1])
        print("Assigned Doctor ID:", n[2])
        print("\n")
    print("All Nurses listed")
    exit()


#------DEPARTMENT QUERIES------
def add_department():
    mycursor = mydb.cursor()
    print('------ Add Department ------\n')
    _Budget = input('Enter Budget of Dept. : ')
    DPName = input('Enter Dept. Name : ')
    HDID = input('Enter Head-Doctor ID: ')

    #sql in here too
    #come back and check if Doctor id's exist
    sql = 'INSERT INTO `Department` (`budget`,`dp_name`,`hd_id`) VALUES (%s, %s, %s)'
    val = (_Budget, DPName, HDID)
    mycursor.execute(sql,val)
    mydb.commit()

    print('------ SUCCESS ------\n')
    exit()

def modify_department():
    mycursor = mydb.cursor()
    modify_department_menu()
    n = int(input("Insert option: "))

    if n == 1:
    # Select Dname
        os.system("cls")
        deptname = input('Enter Dept. name : ')
        _Budget = input('Enter Budget of Dept. : ')
        HDID = input('Enter Head-Doctor ID : ')

        #sql in here too
        sql = 'UPDATE `DEPARTMENT` SET BUDGET=%s, SET HD_ID=%s, WHERE dp_name=%s' % (deptname)
        val = (_Budget, HDID, deptname)
        mycursor.execute(sql,val)
        mydb.commit()

        print('------ SUCCESS ------\n')
        exit()
    elif n == 2:
    #Select Dnum/ID
        os.system("cls")
        dnum = input('Enter Dept. Number name : ')
        _Budget = input('Enter Budget of Dept. : ')
        HDID = input('Enter Head-Doctor ID : ')

        sql = 'UPDATE `DEPARTMENT` SET BUDGET = %s, SET HD_ID=%s, WHERE dept_num=%s'
        val = (_Budget, HDID, dnum)
        mycursor.execute(sql,val)
        mydb.commit()

        print('------ SUCCESS ------\n')
        exit()
    elif n == 3:
        os.system("cls")
        #go back
        exit()
    else:
        os.system("cls")
        modify_department()
def modify_department_menu():
    print('------ Modify Department ------\n')
    print('1. Modify via Name of Dept.')
    print('2. Modify via Dept. ID')
    print('3. Back')

def delete_department():
    mycursor = mydb.cursor()
    delete_department_menu()
    n = int(input("Insert option:"))

    if n == 1:
        os.system("cls")
        deptname = input('Enter Dept. name : ')

        #sql in here too
        sql = 'DELETE FROM DEPARTMENT WHERE dp_name=%s' % (deptname)
        mycursor.execute(sql)
        mydb.commit()

        print('------ SUCCESS ------\n')
        exit()
    elif n == 2:
        os.system("cls")
        dnum = input('Enter Dept. Number name : ')

        #sql goes here
        sql = 'DELETE FROM DEPARTMENT WHERE dept_num=%s' % (dnum)
        mycursor.execute(sql)
        mydb.commit()

        print('------ SUCCESS ------\n')
        exit()
    elif n == 3:
        os.system("cls")
        #go back
        exit()
    else:
        os.system("cls")
        delete_department()

    print('------ SUCCESS ------\n')
    exit()
def delete_department_menu():
    print('------ Delete Department ------\n')
    print('1. Delete via Name of Dept.')
    print('2. Delete via Dept. ID')
    print('3. Back')

def showDepts():
    mycursor = mydb.cursor()
    print("--All Departments--\n")
    mycursor.execute('SELECT * FROM department')
    deptList = mycursor.fetchall()
    for d in deptList:
        print("--Department", d[0], "--")
        print("Budget: $", d[1])
        print("Name:", d[2])
        print("Head Doctor ID:", d[3])
        print("\n")
    print("All Departments listed")
    exit()


#------SURGERY QUERIES------
def showSurgeries():
    mycursor = mydb.cursor()
    print("--All Surgeries--\n")
    mycursor.execute('SELECT * FROM surgery')
    surgeryList = mycursor.fetchall()
    for s in surgeryList:
        print("--Surgery", s[0], "--")
        print("Mortality Rate:", s[1], "%")
        print("Surgery Type:", s[2])
        print("Cost: $", s[3])
        print("\n")
    print("All Surgeries listed")
    exit()


#------AGGREGATE FUNCTION------
def avgMort():
    mycursor = mydb.cursor()
    print('------ Avg Mortality ------\n')
    sql = 'SELECT AVG(mortality_rate) FROM `Surgery`'
    mycursor.execute(sql)
    result = mycursor.fetchone();
    format_result="{:.2f}".format(result[0])
    print(format_result,"%",sep="")
    exit()

def avgCost():
    mycursor = mydb.cursor()
    print('------ Average Cost of All Surgeries ------\n')
    sql = 'SELECT AVG(cost) FROM `Surgery`'
    mycursor.execute(sql)
    result = mycursor.fetchone();
    format_result="{:.2f}".format(result[0])
    print("$",format_result,sep="")
    exit()

def maxBudget():
    mycursor = mydb.cursor()
    print("------Max Department Budget of Hospital------\n")
    sql = 'SELECT budget FROM department WHERE budget = (SELECT MAX(budget) FROM department)'
    mycursor.execute(sql)
    result = mycursor.fetchone()
    format_result = "{:.2f}".format(result[0])
    print("$", format_result,sep="")
    exit()


#------CONDUCTS------
def assign_procedure():
    mycursor = mydb.cursor()
    print('------ Assign Procedure ------\n')
    surg=input("What type of Surgery : ")
    Dname=input("What Doctor [Their Name] : ")
    sql = 'SELECT surgery_id FROM `Surgery` WHERE type_of="%s"' % (surg)
    mycursor.execute(sql)
    val1 = mycursor.fetchone();
    val1=val1[0]
    sql='SELECT id FROM `Doctor` WHERE name="%s"' % (Dname)
    mycursor.execute(sql)
    val2 = mycursor.fetchone();
    sql = 'INSERT INTO `conducts` VALUES (%s,%s)'
    val = (val1, val2)
    mycursor.execute(sql,val)
    mydb.commit()
    exit()


#------UNDERGOES------
def conduct_surgury():
    mycursor = mydb.cursor()
    print('------ Conduct Surgury ------\n')
    surg=input("What type of Surgery : ")
    PID=input("What Patient [Their ID] : ")
    sql = 'SELECT surgery_id FROM Surgery WHERE type_of="%s"' % (surg)
    mycursor.execute(sql)
    val1 = mycursor.fetchone();
    val1=val1[0]
    sql = 'INSERT INTO UNDERGOES VALUES (%s,%s)'
    val = (val1, PID)
    mycursor.execute(sql,val)
    mydb.commit()
    exit()


#------WORKS_FOR------
def worksFor():
    mycursor = mydb.cursor()
    print("----Set Doctor to Department----")
    showDoctors()
    doctorID = int(input("Doctor ID to choose where they work? "))
    showDepts()
    deptID = int(input("Department ID in Which they will work in? "))
    sql = 'INSERT INTO works_for (doctorID, deptID) VALUES (%s,%s)'
    val(doctorID, deptID)
    mycursor.execute(sql,val)
    mydb.commit()
    exit()


#------TREATS------
def treats():
    mycursor = mydb.cursor()
    print("----Doctor treating Patients----")
    showPatients()
    patientID = int(input("Patient ID being treated? "))
    showDoctors()
    doctorID = int(input("Doctor ID to treat Patient? "))
    sql = 'INSERT INTO treats (patientID, doctorID) VALUES (%s,%s)'
    val(patientID, doctorID)
    mycursor.execute(sql,val)
    mydb.commit()
    exit()


#------SURGERY COMPLETE------
def surgury_complete():
    mycursor = mydb.cursor()
    print('------ Complete Surgury ------\n')
    surg=input("What type of Surgery : ")
    P_ID=input("What Patient [Their ID] : ")
    sql = 'SELECT surgery_id FROM Surgery WHERE type_of="%s"' % (surg)
    mycursor.execute(sql)
    val1 = mycursor.fetchone();
    val1=val1[0]
    sql = 'DELETE FROM undergoes WHERE (sid="%s" AND pid=%s)'
    val = (val1, int(P_ID))
    mycursor.execute(sql,val)
    mydb.commit()
    exit()







#------EXECUTES------
def run():
    displayMainMenu()
    choice = int(input("Please choose an option: "))
    if choice == 0:
        os.system('cls')
        print("--Thank You--")
    elif choice == 1: #Patient Submenu
        os.system('cls')
        displayPatientMenu()
        subchoice = int(input("Please choose an option: "))
        if subchoice == 0: #exit
            os.system('cls')
            print("--Returning to main menu--")
            exit()
        elif subchoice == 1: #Add
            os.system('cls')
            addPatient()
        elif subchoice == 2: #Modify
            os.system('cls')
            modify_patient()
        elif subchoice == 3: #Discharge
            os.system('cls')
            dischargePatient()
        elif subchoice == 4: #Show All
            os.system('cls')
            showPatients()
        else:                #other
            os.system('cls')
            run()
    elif choice == 2: #Employee Submenu
        os.system('cls')
        displayEmployeeMenu()
        subchoice = int(input("Please choose an option: "))
        if subchoice == 0: #exit
            os.system('cls')
            print("--Returning to main menu--")
            exit()
        elif subchoice == 1: #Hire
            os.system('cls')
            hire_employee()
        elif subchoice == 2: #Fire
            os.system('cls')
            fire_employee()
        elif subchoice == 3: #Modify
            os.system('cls')
            modify_employee()
        elif subchoice == 4: #Reassign Nurse
            os.system('cls')
            reassign_nurse()
        elif subchoice == 5: #Show Doctor
            os.system('cls')
            showDoctors()
        elif subchoice == 6: #Show Nurse
            os.system('cls')
            showNurses()
        else:                #other
            os.system('cls')
            run()
    elif choice == 3: #Department Submenu
        os.system('cls')
        displayDepartmentMenu()
        subchoice = int(input("Please choose an option: "))
        if subchoice == 0: #exit
            os.system('cls')
            print("--Return to main menu--")
            exit()
        elif subchoice == 1: #Add
            os.system('cls')
            add_department()
        elif subchoice == 2: #Modify
            os.system('cls')
            modify_department()
        elif subchoice == 3: #Delete
            os.system('cls')
            delete_department()
        elif subchoice == 4: #Show All
            os.system('cls')
            showDepts()
        else:                #other
            os.system('cls')
            run()
    elif choice == 4: #Surgery Submenu
        os.system('cls')
        displaySurgeryMenu()
        subchoice = int(input("Please choose an option: "))
        if subchoice == 0: #exit
            os.system('cls')
            exit()
        elif subchoice == 1: #Show All
            os.system('cls')
            showSurgeries()
        else:                #other
            os.system('cls')
            run()
    elif choice == 5: #Conducts
        os.system('cls')
        assign_procedure()
    elif choice == 6: #Undergoes
        os.system('cls')
        conduct_surgury()
    elif choice == 7: #Works_For
        os.system('cls')
        worksFor()
    elif choice == 8: #Treats
        os.system('cls')
        treats()
    elif choice == 9: #Surgery Complete
        os.system('cls')
        surgury_complete()
    elif choice == 10: #Aggregate Function Submenu
        os.system('cls')
        displayAgFuncMenu()
        subchoice = int(input("Please choose an option: "))
        if subchoice == 0: #exit
            os.system('cls')
            print("--Returning to main menu--")
            exit()
        elif subchoice == 1: #Average Mortality
            os.system('cls')
            avgMort()
        elif subchoice == 2: #Average Cost
            os.system('cls')
            avgCost
        elif subchoice == 3: #Max Budget
            os.system('cls')
            maxBudget()
        else:                #other
            os.system('cls')
            run()
    else:             #other
        os.system('cls')
        run()

if __name__ == "__main__":
    initDB()
    run()