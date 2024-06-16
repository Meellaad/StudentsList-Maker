# Milad Pourvali Andarabi

from os import system


# student_list = []
student_list = [
    ["milad", "karimi", "0991", "4413", "78934", "male", "a", 33, "tehran", "single", [65.0, 90.0, 70.0]],
    ["dorsa", "niazi", "0912", "4378", "87432", "female", "b", 18, "tabriz", "single", [75.0, 100.0, 67.0]],
    ["milad", "ahmadi", "0936", "5987", "53789", "male", "c", 29, "karaj", "married", [45.0, 78.0, 95.0]],
    ["mahsa", "karami", "0914", "1294", "43028", "female", "d", 24, "rasht", "single", [56.0, 71.0, 90.0]],
    ["ahmad", "naad", "0902", "1572", "33705", "male", "e", 45, "ahvaz", "married", [94.0, 93.0, 86.0]],
    ["sara", "safari", "0903", "3367", "99663", "female", "a", 51, "qom", "married", [94.0, 90.0, 40.0]],
    ["sima", "sabeti", "0904", "7688", "82347", "female", "b", 22, "yazd", "single", [38.0, 65.0, 95.0]],
    ["taha", "emami", "0905", "4512", "10123", "male", "d", 30, "sari", "single", [94.0, 100.0, 50.0]],
    ["nima", "moradi", "0913", "9056", "65238", "male", "c", 39, "kerman", "married", [85.0, 66.0, 95.0]],
    ["ali", "rahimi", "0939", "1499", "22545", "other", "e", 45, "kish", "single", [94.0, 90.0, 89.0]],
]

continue_ = True

while continue_:

    print("\nMenu")
    print("--------------")
    print("1. Add")
    print("2. Show")
    print("3. Remove")
    print("4. Edit")
    print("5. Search")
    print("6. Besties")
    print("7. Quit")
    print("--------------\n")

    menu = input("Menu: ")
    system("clear")


    if menu not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Error!!! Try Again...")

    elif menu=="1":
        continue_add = True

        while continue_add:
            system("clear")

            answer = input("Do you want to add a student? (yes | etc) : ")

            if answer!="yes":
                continue_add = False
                system("clear")

            else:
                system("clear")

                #region get firstname
                flag = True

                while flag: 
                    first_name = input("Firstname: ")
                    system("clear")

                    if first_name=="":
                        print("Error! Firstname is empty!!")

                    else:
                        flag = False
                #endregion

                #region get lastname
                flag = True

                while flag: 
                    last_name = input("Lastname: ")
                    system("clear")


                    if last_name=="":
                        print("Error! Lastname is empty!!")

                    else:
                        flag = False
                #endregion
                        
                #region get phone number
                flag = True

                while flag: 
                    phone_number = input("Phone Number: ")
                    system("clear")


                    if phone_number!="":
                        check_unique = True
                        i = 0

                        while check_unique and i<len(student_list):
                            student = student_list[i]

                            if student[2]==phone_number:
                                check_unique = False
                            
                            i += 1

                        if check_unique:
                            flag = False
                        else:
                            print(phone_number, "Exists!")

                    else:
                        print("Error! Phone Number is empty!!")
                #endregion
                        
                #region get student code
                flag = True

                while flag: 
                    student_code = input("Student Code: ")
                    system("clear")


                    if student_code!="":
                        check_unique = True
                        i = 0

                        while check_unique and i<len(student_list):
                            student = student_list[i]

                            if student[3]==student_code:
                                check_unique = False
                            
                            i += 1

                        if check_unique:
                            flag = False
                        else:
                            print(student_code, "Exists!")

                    else:
                        print("Error! Student Code is empty!!")
                #endregion
                        
                #region get national code
                flag = True

                while flag: 
                    national_code = input("National Code: ")
                    system("clear")


                    if national_code!="":
                        check_unique = True
                        i = 0

                        while check_unique and i<len(student_list):
                            student = student_list[i]

                            if student[4]==national_code:
                                check_unique = False
                            
                            i += 1

                        if check_unique:
                            flag = False
                        else:
                            print(national_code, "Exists!")

                    else:
                        print("Error! National Code is empty!!")
                #endregion
                        
                #region get gender
                flag = True

                while flag:
                    gender = input("Gender( male | female | other): ")
                    system("clear")

                    if gender=="":
                        print("Error! Gender is empty!!")

                    elif gender not in ["male", "female", "other"]:
                        print("Error!! gender is wrong ")

                    else:
                        flag = False
                #endregion

                #region get class
                flag = True

                while flag:
                    class_ = input("Class( a | b | c | d | e): ")
                    system("clear")

                    if class_=="":
                        print("Error! Class is empty!!")

                    elif class_ not in ["a", "b", "c", "d", "e"]:
                        print("Error!! class is wrong ")

                    else:
                        flag = False
                #endregion

                #region get age
                flag = True

                while flag: 
                    age = int(input("Age (1 - 120): "))
                    system("clear")

                    if 0<age<=120:
                        flag = False
                    else: 
                        print("Error!! enter a number between 1 to 120")
                #endregion
                        
                #region get adress
                address = input("Address: ")
                system("clear")
                #endregion

                #region get description
                description = input("Description: ")
                system("clear")
                #endregion
                        
                #region get java score
                flag = True

                while flag: 
                    java = float(input("Java score (0 - 100): "))
                    system("clear")

                    if 0<=java<=100:
                        flag = False
                    else: 
                        print("Error!! enter a number between 0 to 100")
                #endregion
                        
                #region get python score
                flag = True

                while flag: 
                    python = float(input("Python score (0 - 100): "))
                    system("clear")

                    if 0<=python<=100:
                        flag = False
                    else: 
                        print("Error!! enter a number between 0 to 100")
                #endregion

                #region get php score
                flag = True

                while flag: 
                    php = float(input("Php score (0 - 100): "))
                    system("clear")

                    if 0<=php<=100:
                        flag = False
                    else: 
                        print("Error!! enter a number between 0 to 100")
                #endregion

                #region set data
                student = [first_name, last_name, phone_number, student_code, national_code, gender, class_, age, address, description]
                scores = [java, python, php]
                student.append(scores)
                student_list.append(student)
                #endregion

    elif menu=="2":
        
        continue_show = True

        while continue_show:

            reply = input("Do you want to see the student's list (yes | etc)? ")
            system("clear")

            if reply=="yes":

                answer = input("Do you want to display all students (yes | etc)? ")
                system("clear")


                if answer=="yes":
                    print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                    print("No.", "Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    No_ = 1

                    for student in student_list:
                        i = 0
                        print(No_, end="\t")
                        
                        while i<len(student)-1:
                            print(student[i], sep="\t", end="\t")
                            
                            i += 1

                            if i==10:
                                j = 0
                                while j<len(student[i]):
                                    print(student[i][j], sep="\t", end="\t")

                                    j += 1

                                print()

                        No_ += 1



                    print("-----------------------------------------------------------------------------------------------------------------------------------\n")
                else:
                    title_list = ["Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php"]
                    header_list = ["No."]
                    index_list = []
                    index = 0

                    for title in title_list:
                        print("Do you want to display", title, "(yes | etc) ?", end=" ")
                        system("clear")

                        if input()=="yes":
                            header_list.append(title)
                            index_list.append(index)

                        index += 1

                    #region show result
                    if len(index_list)!=0:
                        system("clear")

                        print("\n-----------------------------------------------------------------------------------------------------------------------------------")

                        for header in header_list:
                            print(header, end="\t")

                        print("\n-----------------------------------------------------------------------------------------------------------------------------------")

                        No_ = 1

                        for student in student_list:
                            print(No_, end="\t")

                            for index in index_list:

                                if index<10:
                                    print(student[index], end="\t")
                                    
                                if index==10:
                                    print(student[10][0], end="\t")

                                if index==11:
                                    print(student[10][1], end="\t")

                                if index==12:
                                    print(student[10][2], end="\t")

                            print()
                            No_ += 1

                        print()

                    else:
                        print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                        print("No.", "Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                        print("-----------------------------------------------------------------------------------------------------------------------------------\n")
                    #endregion
                        
            else:
                continue_show = False

    elif menu=="3":
                
        continue_remove = True

        while continue_remove:
            system("clear")

            answer = input("Do you want to remove a student? (yes | etc): ")
            system("clear")

            if answer!="yes":
                continue_remove = False
                system("clear")

            else:
                temp = True

                while temp:
                    print("\nPlease select your method to remove:")
                    print("1. By Phone Number")
                    print("2. By Student Code")
                    print("3. By National Code")
                    print("4. Exit")

                    remove_menu = input()
                    system("clear")

                    if remove_menu not in ["1", "2", "3", "4"]:
                        system("clear")
                        print("Error! Input is wrong, Try Again...")

                    else:
                        system("clear")

                        if remove_menu=="4":
                            temp = False

                        elif remove_menu=="1":

                            #region get phone number
                            flag = True

                            while flag: 
                                phone_number = input("Phone Number: ")
                                system("clear")


                                if phone_number!="":
                                    check_exist = True
                                    i = 0

                                    while check_exist and i<len(student_list):
                                        student = student_list[i]

                                        if student[2]==phone_number:
                                            student_list.remove(student_list[i])
                                            print("Done")
                                            check_exist = False
                                        
                                        i += 1

                                    if check_exist:
                                        print(phone_number, "not found!")

                                    else:
                                        flag = False

                                else:
                                    print("Error! Phone Number is empty!!")
                                    flag = False
                            #endregion

                        elif remove_menu=="2":

                            #region get student code
                            flag = True

                            while flag: 
                                student_code = input("Student Code: ")
                                system("clear")


                                if student_code!="":
                                    check_exist = True
                                    i = 0

                                    while check_exist and i<len(student_list):
                                        student = student_list[i]

                                        if student[3]==student_code:
                                            student_list.remove(student_list[i])
                                            print("Done")
                                            check_exist = False
                                        
                                        i += 1

                                    if check_exist:
                                        print(student_code, "not found!")

                                    else:
                                        flag = False

                                else:
                                    print("Error! Student Code is empty!!")
                                    flag = False
                            #endregion

                        else:
                            
                            #region get national code
                            flag = True

                            while flag: 
                                national_code = input("National Code: ")
                                system("clear")


                                if national_code!="":
                                    check_exist = True
                                    i = 0

                                    while check_exist and i<len(student_list):
                                        student = student_list[i]

                                        if student[4]==national_code:
                                            student_list.remove(student_list[i])
                                            print("Done")
                                            check_exist = False
                                        
                                        i += 1

                                    if check_exist:
                                        print(national_code, "not found!")

                                    else:
                                        flag = False

                                else:
                                    print("Error! National Code is empty!!")
                                    flag = False
                            #endregion

    elif menu=="4":
                
        continue_edit = True

        while continue_edit:
            system("clear")

            #region show the list
            print("\n-----------------------------------------------------------------------------------------------------------------------------------")
            print("No.", "Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
            print("-----------------------------------------------------------------------------------------------------------------------------------")
            No_ = 1

            for student in student_list:
                i = 0
                print(No_, end="\t")
                
                while i<len(student)-1:
                    print(student[i], sep="\t", end="\t")
                    
                    i+=1

                    if i==10:
                        j = 0
                        while j<len(student[i]):
                            print(student[i][j], sep="\t", end="\t")

                            j+=1

                        print()

                No_ += 1
                #endregion

            answer = input("\nDo you want edit a student data? (yes | etc): ")
            system("clear")
                
            if answer!="yes":
                    continue_edit = False
                    system("clear")

            else:

                print("\nPlease select your method to find and edit:")
                print("1. By Phone Number")
                print("2. By Student Code")
                print("3. By National Code")
                print("4. Exit")

                edit_menu = input()
                system("clear")

                if edit_menu not in ["1", "2", "3", "4"]:
                    system("clear")

                elif edit_menu=="4":
                    continue_edit = False

                else:
                    system("clear")
                    flag = True
                    temp = True

                    if edit_menu=="1":

                        #region get phone number
                        while flag: 
                            phone_number = input("Phone Number | Press Enter to exit: ")
                            system("clear")


                            if phone_number!="":
                                check_exist = True
                                index = 0

                                while check_exist and index<len(student_list):
                                    student = student_list[index]

                                    if student[2]==phone_number:

                                        current_student = student_list[index]
                                        
                                        #region show the student
                                        print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                                        print("Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                                        
                                        st_index = 0

                                        while st_index<len(student)-1:
                                            print(student_list[index][st_index], sep="\t", end="\t")

                                            st_index+=1

                                            if st_index==10:
                                                score_index = 0

                                                while score_index<len(student[st_index]):
                                                    print(student[st_index][score_index], sep="\t", end="\t")

                                                    score_index+=1

                                                print()

                                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                                        #endregion

                                        check_exist = False
                                    
                                    index+=1

                                if check_exist:
                                    print(phone_number, "not found!")

                                else:
                                    flag = False

                            else:
                                temp = False
                                flag = False
                        #endregion

                    elif edit_menu=="2":

                        #region get student code
                        while flag: 
                            student_code = input("Student Code | Press Enter to exit: ")
                            system("clear")


                            if student_code!="":
                                check_exist = True
                                index = 0

                                while check_exist and index<len(student_list):
                                    student = student_list[index]

                                    if student[3]==student_code:

                                        current_student = student_list[index]
                                        
                                        #region show the student
                                        print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                                        print("Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                                        
                                        st_index = 0

                                        while st_index<len(student)-1:
                                            print(student_list[index][st_index], sep="\t", end="\t")

                                            st_index+=1

                                            if st_index==10:
                                                score_index = 0

                                                while score_index<len(student[st_index]):
                                                    print(student[st_index][score_index], sep="\t", end="\t")

                                                    score_index+=1

                                                print()

                                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                                        #endregion

                                        check_exist = False
                                    
                                    index+=1

                                if check_exist:
                                    print(student_code, "not found!")

                                else:
                                    flag = False

                            else:
                                temp = False
                                flag = False
                        #endregion

                    else:
                        
                        #region get national code
                        while flag: 
                            national_code = input("National Code | Press Enter to exit: ")
                            system("clear")


                            if national_code!="":
                                check_exist = True
                                index = 0

                                while check_exist and index<len(student_list):
                                    student = student_list[index]

                                    if student[4]==national_code:

                                        current_student = student_list[index]
                                        
                                        #region show the student
                                        print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                                        print("Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                                        
                                        st_index = 0

                                        while st_index<len(student)-1:
                                            print(student_list[index][st_index], sep="\t", end="\t")

                                            st_index+=1

                                            if st_index==10:
                                                score_index = 0

                                                while score_index<len(student[st_index]):
                                                    print(student[st_index][score_index], sep="\t", end="\t")

                                                    score_index+=1

                                                print()

                                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                                        #endregion

                                        check_exist = False
                                    
                                    index+=1

                                if check_exist:
                                    print(national_code, "not found!")

                                else:
                                    flag = False

                            else:
                                temp = False
                                flag = False
                        #endregion


                    #region edit menu
                    while temp:

                        print("\nWhich one do you want to edit?")
                        print("1. First Name")
                        print("2. Last Name")
                        print("3. Phone Number")
                        print("4. Student Code")
                        print("5. National Code")
                        print("6. Gender")
                        print("7. Class")
                        print("8. Age")
                        print("9. Address")
                        print("10. Description")
                        print("11. Java Score")
                        print("12. Python Score")
                        print("13. PHP Score")
                        print("14. Exit")

                        selected_edit_item = input()
                        system("clear")

                        if selected_edit_item not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]:
                            print("Error! Input is incorrect, Try Again...")
                            temp = False

                        elif selected_edit_item=="14":
                            temp = False

                        else:

                            if selected_edit_item=="1":

                            #region get new first name
                                new_first_name = input("New First Name: ")

                                if new_first_name=="":
                                    system("clear")
                                    print("Sorry, This field cannot be empty.")

                                else:
                                    current_student[0] = new_first_name
                                    system("clear")
                                    print("Done")
                            #endregion

                            elif selected_edit_item=="2":

                            #region get new last name
                                new_last_name = input("New Last Name: ")

                                if new_last_name=="":
                                    system("clear")
                                    print("Sorry, This field cannot be empty.")

                                else:
                                    current_student[1] = new_last_name
                                    system("clear")
                                    print("Done")
                            #endregion

                            elif selected_edit_item=="3":

                                #region get new phone number
                                new_phone_number = input("New Phone Number: ")

                                if new_phone_number=="":
                                    system("clear")
                                    print("Sorry, This field cannot be empty.")

                                else:
                                    
                                    if current_student[2]==new_phone_number:
                                        current_student[2] = new_phone_number
                                        system("clear")
                                        print("Done")

                                    else:
                                        check_unique = True
                                        s_index = 0

                                        while check_unique and s_index<len(student_list):

                                            if student_list[s_index][2]==new_phone_number:
                                                check_unique = False

                                            s_index += 1

                                        if check_unique:
                                            current_student[2] = new_phone_number
                                            system("clear")
                                            print("Done")
                                        
                                        else:
                                            system("clear")
                                            print("Sorry, You cannot change it.", new_phone_number, "is exist.")
                                #endregion

                            elif selected_edit_item=="4":

                                #region get new student code
                                new_student_code = input("New Student Code: ")

                                if new_student_code=="":
                                    system("clear")
                                    print("Sorry, This field cannot be empty.")

                                else:
                                    
                                    if current_student[3]==new_student_code:
                                        current_student[3] = new_student_code
                                        system("clear")
                                        print("Done")

                                    else:
                                        check_unique = True
                                        s_index = 0

                                        while check_unique and s_index<len(student_list):

                                            if student_list[s_index][3]==new_student_code:
                                                check_unique = False

                                            s_index += 1

                                        if check_unique:
                                            current_student[3] = new_student_code
                                            system("clear")
                                            print("Done")
                                        
                                        else:
                                            system("clear")
                                            print("Sorry, You cannot change it.", new_student_code, "is exist.")
                                #endregion

                            elif selected_edit_item=="5":

                                #region get new national code
                                new_national_code = input("New National Code: ")

                                if new_national_code=="":
                                    system("clear")
                                    print("Sorry, This field cannot be empty.")

                                else:
                                    
                                    if current_student[4]==new_national_code:
                                        current_student[4] = new_national_code
                                        system("clear")
                                        print("Done")

                                    else:
                                        check_unique = True
                                        s_index = 0

                                        while check_unique and s_index<len(student_list):

                                            if student_list[s_index][4]==new_national_code:
                                                check_unique = False

                                            s_index += 1

                                        if check_unique:
                                            current_student[4] = new_national_code
                                            system("clear")
                                            print("Done")
                                        
                                        else:
                                            system("clear")
                                            print("Sorry, You cannot change it.", new_national_code, "is exist.")
                                #endregion                                            

                            elif selected_edit_item=="6":

                                #region get new gender
                                new_gender = input("New Gender( male | female | other): ")

                                if new_gender=="":
                                    system("clear")
                                    print("Sorry, this field connot be empty.")

                                elif new_gender not in ["male", "female", "other"]:
                                    system("clear")
                                    print("Error! Gender must be male or female or other.")

                                else:
                                    current_student[5] = new_gender
                                    system("clear")
                                    print("Done")
                                #endregion

                            elif selected_edit_item=="7":

                                #region get new class
                                new_class = input("New Class( a | b | c | d | e): ")

                                if new_class=="":
                                    system("clear")
                                    print("Sorry, this field connot be empty.")

                                elif new_class not in ["a", "b", "c", "d", "e"]:
                                    system("clear")
                                    print("Error! Class must be a, b, c, d or e.")

                                else:
                                    current_student[6] = new_class
                                    system("clear")
                                    print("Done")
                                #endregion

                            elif selected_edit_item=="8":

                                #region get new age
                                new_age = int(input("New Age (1 - 120): "))

                                if new_age not in range (1, 121):
                                    system("clear")
                                    print("Sorry, the number must be between 1 to 120.")

                                else:
                                    current_student[7] = new_age
                                    system("clear")
                                    print("Done")
                                #endregion

                            elif selected_edit_item=="9":

                                #region get new address
                                new_address = input("New Address: ")
                                current_student[8] = new_address
                                system("clear")
                                print("Done")
                                #endregion

                            elif selected_edit_item=="10":

                                #region get new description
                                new_description = input("New Description: ")
                                current_student[9] = new_description
                                system("clear")
                                print("Done")
                                #endregion

                            elif selected_edit_item=="11":

                                #region get new java score
                                new_java_score = float(input("New Java Score (0 - 100): "))

                                if new_java_score<0 or new_java_score>100 :
                                    system("clear")
                                    print("Sorry, the number must be between 0 to 100.")

                                else:
                                    current_student[10][0] = new_java_score
                                    system("clear")
                                    print("Done")
                                #endregion

                            elif selected_edit_item=="12":

                                #region get new python score
                                new_python_score = float(input("New Python Score (0 - 100): "))

                                if new_python_score<0 or new_python_score>100 :
                                    system("clear")
                                    print("Sorry, the number must be between 0 to 100.")

                                else:
                                    current_student[10][1] = new_python_score
                                    system("clear")
                                    print("Done")
                                #endregion

                            else:

                                #region get new php score
                                new_php_score = float(input("New PHP Score (0 - 100): "))

                                if new_php_score<0 or new_php_score>100 :
                                    system("clear")
                                    print("Sorry, the number must be between 0 to 100.")

                                else:
                                    current_student[10][2] = new_php_score
                                    system("clear")
                                    print("Done")
                                #endregion
                                    

                            #region show result
                            print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                            print("Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                            print("-----------------------------------------------------------------------------------------------------------------------------------")

                            cs_index = 0

                            while cs_index<len(current_student)-1:
                                print(current_student[cs_index], sep="\t", end="\t")

                                cs_index += 1

                                if cs_index==10:
                                    for score in current_student[10]:
                                        print(score, sep="\t", end="\t")

                                    print()
                            #endregion
                    # endregion

    elif menu=="5":
                
        continue_search = True

        while continue_search:

            answer = input("Do you want to search? (yes | etc): ")

            if answer!="yes":
                continue_search = False
                system("clear")

            else:
                system("clear")
                print("\nWhat do you want to search based on?")
                print("1. By First Name")
                print("2. By Last Name")
                print("3. By Phone Number")
                print("4. By Student Code")
                print("5. By National Code")
                print("6. By Gender")
                print("7. By Class")
                print("8. By Age")
                print("9. Exit")

                search_menu = input()
                system("clear")

                if search_menu not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    system("clear")
                    print("Error! Input is wrong, Try Again...")

                elif search_menu=="9":
                    continue_search = False

                else:
                    #region get search value
                    if search_menu=="1":
                        search_value = input("First Name: ")
                        search_index = 0

                    elif search_menu=="2":
                        search_value = input("Last Name: ")
                        search_index = 1

                    elif search_menu=="3":
                        search_value = input("Phone Number: ")
                        search_index = 2

                    elif search_menu=="4":
                        search_value = input("Student Code: ")
                        search_index = 3

                    elif search_menu=="5":
                        search_value = input("National Code: ")
                        search_index = 4

                    elif search_menu=="6":
                        search_value = input("Gender(male | female | other): ")
                        search_index = 5

                    elif search_menu=="7":
                        search_value = input("Class(a | b | c | d | e): ")
                        search_index = 6

                    else:
                        search_value = int(input("Age(1 - 120): "))
                        search_index = 7
                    #endregion
                        
                    #region search and show result
                    print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                    print("No.", "Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                    print("-----------------------------------------------------------------------------------------------------------------------------------")
                    No_ = 1    
                    
                    for student in student_list:

                        if student[search_index]==search_value:
                            i = 0
                            print(No_, end="\t")

                            while i<len(student) and i!=10:
                                print(student[i], sep="\t", end="\t")

                                i += 1

                                if i==10:
                                    for score in student[10]:
                                        print(score, sep="\t", end="\t")

                                    print()

                            No_ += 1
                                

                    print("-----------------------------------------------------------------------------------------------------------------------------------\n")
                    #endregion
                        
    elif menu=="6":

        continue_best = True

        while continue_best:

            answer = input("Do you want to continue? (yes | etc): ")

            if answer!="yes":
                system("clear")
                continue_best = False

            else:

                system("clear")
                temp = True

                while temp:
                    print("\nSelect the best list: ")
                    print("1. Best Java")
                    print("2. Best Python")
                    print("3. Best PHP")
                    print("4. Best Avrage")
                    print("5. Exit")

                    best_menu = input()
                    system("clear")

                    if best_menu not in ["1", "2", "3", "4"] or best_menu=="5":
                        system("clear")
                        temp = False

                    elif best_menu=="4":

                        #region find the best avrage
                        max_avrage = 0

                        for score in student_list[0][10]:
                            max_avrage += score

                        for student in student_list:
                            student_score = 0

                            for score in student[10]:
                                student_score += score

                            if student_score>max_avrage:
                                max_avrage = student_score
                        #endregion

                        #region show result
                        print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                        print("No.", "Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                        No_ = 1

                        for student in student_list:

                            student_score = 0

                            for score in student[10]:
                                student_score += score

                            if student_score==max_avrage:
                                i = 0
                                print(No_, end="\t")

                                while i<len(student) and i!=10:
                                    print(student[i], sep="\t", end="\t")

                                    i += 1

                                    if i==10:
                                        for score in student[i]:
                                            print(score, sep="\t", end="\t")

                                        print()

                                        No_ += 1        

                        print("-----------------------------------------------------------------------------------------------------------------------------------\n")
                        #endregion

                    else:

                        if best_menu=="1":
                            best_index = 0

                        elif best_menu=="2":
                            best_index = 1

                        else:
                            best_index = 2


                        #region find the best score
                        max_score = student_list[0][10][best_index]

                        for student in student_list:

                            if student[10][best_index]>max_score:
                                max_score = student[10][best_index]
                        #endregion
                                
                        #region show result
                        print("\n-----------------------------------------------------------------------------------------------------------------------------------")
                        print("No.", "Name", "Family", "Phone", "STcode", "Ncode", "Gender", "Class", "Age", "Address", "Info", "Java", "Python", "Php", sep="\t")
                        print("-----------------------------------------------------------------------------------------------------------------------------------")
                        No_ = 1

                        for student in student_list:

                            if student[10][best_index]==max_score:
                                i = 0
                                print(No_, end="\t")

                                while i<len(student) and i!=10:
                                    print(student[i], sep="\t", end="\t")

                                    i += 1

                                    if i==10:
                                        for score in student[i]:
                                            print(score, sep="\t", end="\t")

                                        print()

                                        No_ += 1        

                        print("-----------------------------------------------------------------------------------------------------------------------------------\n")
                        #endregion
    
    else:
        continue_ = False
        system("clear")

