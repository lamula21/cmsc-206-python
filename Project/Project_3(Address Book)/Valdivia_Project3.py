# Author: Jose A. Valdivia Rojas
# Course: CMSC 206
# Project 3 - Final Submission


# Header of the Table
table_header = ["NAME:", "E-MAIL:", "PHONE NUMBER:", "SSN:"]


# If file doesn't exist, create a new file  - Mode: append
f = open('Info_Table.csv', 'a')
f.close()

# Read the file, and store the data in a temporary List - Mode: read
import csv
with open('Info_Table.csv','r', newline='') as csv_file:
    csv_reader_object = csv.reader(csv_file)    # Create an object that reads the csv file
    data_list = [ lines for lines in csv_reader_object]  # Read the data from csv file to a new a list of lists

# Add header if the Table is empty
if len(data_list) == 0:
    data_list.append(table_header)



# CONSTANTS
COLUMN_NAME = 0
COLUMN_EMAIL = 1
COLUMN_PHONE = 2
COLUMN_SSN = 3


# SECONDARY FUNCTIONS
def format_name(name):
    return name.title()

def format_phone(phone):
    areaCode = phone[ 0:3]
    exchange = phone[ 3:6]
    line = phone[ 6:10]
    formatted_phone = f"({areaCode}){exchange}-{line}"      # f-String to format phone numbers into (xxx)xxx-xxxx
    return formatted_phone

def format_ssn(ssn):
    threedigits = ssn[ 0:3]
    twodigits = ssn[ 3:5]
    fourdigits = ssn[ 5:9]
    formatted_ssn = f"{threedigits}-{twodigits}-{fourdigits}"   # f-String to format Social Security Number into xxx-xx-xxxx
    return formatted_ssn    

def show_table(data_list):
    print("")
    for eachLine in data_list:
        print("\n{:>25} {:>25} {:>25} {:>25}".format(eachLine[0], eachLine[1], eachLine[2], eachLine[3]))

def write_and_close_program(data):
    with open("Info_Table.csv", 'w', newline="") as file:
        csvwriter = csv.writer(file) # 1. create a csvwriter object
        csvwriter.writerows(data) # 2. write the rest of the data



# Function to update the Table
def update(value, dataList, new_data, new_data_column):
    print("")

    value = value.split(' ')[0].title()     # Get the first word of the string and format it as title

    for eachRow in dataList:
        for eachElement in eachRow:
            if eachElement.find(value) >= 0:
                eachRow[new_data_column] = new_data
            else:
                continue
        
def delete(value, dataList):

    value = value.title()
    i = 0
    for eachRow in dataList:
        for eachElement in eachRow:
            if eachElement.find(value) >= 0:
                dataList.pop(i)
                print("Row deleted...")
                break
        i += 1


# Function to check the input if it's in the table
def search_in_table(input_search, dataList):
    print("")
    input_search = str(input_search)
    dataList = list(dataList)
    input_search = input_search.split(' ')[0].title()

    for eachRow in dataList:
        for eachElement in eachRow:
            if eachElement.find(input_search) >= 0:
                return True
            else:
                continue

    else:   # Didn't find the data...
        print("NO FOUND")
        return False

# Function to return each element of a row
def search_row(input_search, dataList):

    for eachRow in dataList:
        for eachElement in eachRow:
            if eachElement.find(input_search) >= 0:
                return eachRow[0], eachRow[1], eachRow[2], eachRow[3]








# MAIN FUNCTIONS
# Function to Display - Add Entries Menu
def addEntry():
    while True:
        try:
            print("\nAdding an Entry...")
            user = input("Would you like to add an entry into the database (Y/N) ")
            user = user[0].upper()

            if user == 'Y':

                name = input("What is the name of the person: ")
                email = input("What is the email of the person: ")

                # Validate Phone Number
                while True:
                    phone = input("What is the phone number of the person: ")
                    if len(phone) == 10:
                        break
                    else:
                        print("The phone number must have 10 digits")
                        continue

                # Validate Social Security Number
                while True:    
                    ssn = input("What is the Social Security Number of the person: ")
                    if len(ssn) == 9:
                        break
                    else:
                        print("The SSN must have 9 digits")
                        continue
                    

                # Format name, phone number, and ssn
                name_formatted = format_name(name)
                phone_formatted = format_phone(phone)
                ssn_formatted = format_ssn(ssn)

                # Create a row
                row = [name_formatted , email, phone_formatted, ssn_formatted] 

                # Add entry into the database
                data_list.append(row)
                print("Entry added sucessfully...")
                break
            elif user =='N':
                break
        except ValueError:
            print("Wrong answer. Please Try again")

    # Return True if user wants to repeat Menu, otherwise No
    while True:
        try:
            menu_choice= input("\nDo you want to add, update, delete, or search another contact? (Y/N): ")
            if menu_choice[0].upper() == 'Y':
                return True
            elif menu_choice[0].upper() == 'N':
                return False
            else:
                print("\nPlease choose Yes or No. ")
        except ValueError:
            print("\nInvalid answer. Type (Y/N). ")


# Function to Display - Update Entries Menu
def updateEntry():
    print("")
    while True:
        try:    
            print("Search for a contact to UPDATE")
            print("How would you like to search?")
            print("\t1. Name")
            print("\t2. Phone Number")
            user_option = int(input("Enter a number 1-2: "))
            if user_option >= 1 and user_option <= 2:
                break
            else:
                print("Please enter a number between 1 and 2\n")
        except ValueError:
            print("Wrong input. Please enter a valid integer number\n")
    
    
    # 1. Search Name
    if user_option == 1:
        found = False

        while True:
            name_search = input("Which name do you want to search? ")
            found = search_in_table(name_search, data_list)
            if found:
                break
            else:
                print("There is no such data in the file")

        # If contact name is updated
        user_Yes_No = input("Do you want to update contact name? (Y/N) ")
        if user_Yes_No[0].upper() == 'Y':
            new_name = input("Change name to: ")
            new_name = format_name(new_name)
            update(name_search, data_list, new_name, COLUMN_NAME)

            user_Yes_No = input("Do you want to update email address? (Y/N) ")
            if user_Yes_No[0].upper() == 'Y':
                new_email = input("Change email address to: ")
                update(new_name, data_list, new_email, COLUMN_EMAIL)

            user_Yes_No = input("Do you want to update phone number? (Y/N) ")
            if user_Yes_No[0].upper() == 'Y':
                new_phone = input("Change phone number to: ")
                new_phone = format_phone(new_phone)
                update(new_name, data_list, new_phone, COLUMN_PHONE)

            user_Yes_No = input("Do you want to update SSN? (Y/N) ")
            if user_Yes_No[0].upper() == 'Y':
                new_ssn = input("Change SNN to: ")
                new_ssn = format_ssn(new_ssn)
                update(new_name, data_list, new_ssn, COLUMN_SSN)

        # If contact name is not updated
        elif user_Yes_No[0].upper() == 'N':
            user_Yes_No = input("Do you want to update email address? (Y/N) ")
            if user_Yes_No[0].upper() == 'Y':
                new_email = input("Change email address to: ")
                update(name_search, data_list, new_email, COLUMN_EMAIL)

            user_Yes_No = input("Do you want to update phone number? (Y/N) ")
            if user_Yes_No[0].upper() == 'Y':
                new_phone = input("Change phone number to: ")
                new_phone = format_phone(new_phone)
                update(name_search, data_list, new_phone, COLUMN_PHONE)

            user_Yes_No = input("Do you want to update SSN? (Y/N) ")
            if user_Yes_No[0].upper() == 'Y':
                new_ssn = input("Change SNN to: ")
                new_ssn = format_ssn(new_ssn)
                update(name_search, data_list, new_ssn, COLUMN_SSN)

    # 2. Search Phone Number
    if user_option == 2:

        while True:
            phone_search = input("Which phone number do you want to search? ")
            phone_search = format_phone(phone_search)
            found = search_in_table(phone_search, data_list)
            if found:
                break
            else:
                continue

        user_Yes_No = input("Do you want to update contact name? (Y/N) ")
        if user_Yes_No[0].upper() == 'Y':
            new_name = input("Change name to: ")
            new_name = format_name(new_name)
            update(phone_search, data_list, new_name, COLUMN_NAME)

        user_Yes_No = input("Do you want to update email address? (Y/N) ")
        if user_Yes_No[0].upper() == 'Y':
            new_email = input("Change email address to: ")
            update(phone_search, data_list, new_email, COLUMN_EMAIL)

        # If phone number is updated
        user_Yes_No = input("Do you want to update phone number? (Y/N) ")
        if user_Yes_No[0].upper() == 'Y':
            new_phone = input("Change phone number to: ")
            new_phone = format_phone(new_phone)
            update(phone_search, data_list, new_phone, COLUMN_PHONE)

            user_Yes_No = input("Do you want to update SSN? (Y/N) ")
            if user_Yes_No[0].upper() == 'Y':
                new_ssn = input("Change SNN to: ")
                new_ssn = format_ssn(new_ssn)
                update(new_phone, data_list, new_ssn, COLUMN_SSN)

        # If phone number is not updated        
        elif user_Yes_No[0].upper() == 'N':
            user_Yes_No = input("Do you want to update SSN? (Y/N) ")
            if user_Yes_No[0].upper() == 'Y':
                new_ssn = input("Change SNN to: ")
                new_ssn = format_ssn(new_ssn)
                update(phone_search, data_list, new_ssn, COLUMN_SSN)

    # Return True if user wants to repeat Menu, otherwise No
    while True:
        try:
            menu_choice= input("Do you want to add, update, delete, or search another contact? (Y/N): ")
            if menu_choice[0].upper() == 'Y':
                return True
            elif menu_choice[0].upper() == 'N':
                return False
            else:
                print("\nPlease choose Yes or No. ")
        except ValueError:
            print("\nInvalid answer. Type (Y/N). ")




# Function to display - Delete Entries Menu
def deleteEntry():
    print("")
    while True:
        try:    
            print("Search for a contact to DELETE")
            print("How would you like to search?")
            print("\t1. Name")
            print("\t2. Phone Number")
            print("\t3. Social Security Number")
            user_option = int(input("Enter a number 1-3: "))
            if user_option >= 1 and user_option <= 3:
                break
            else:
                print("Please enter a number between 1 and 3\n")
        except ValueError:
            print("Wrong input. Please enter a valid integer number\n")

    # 1. Search Name
    if user_option == 1:
        found = False

        while True:
            name_search = input("Which name do you want to search? ")
            found = search_in_table(name_search, data_list)
            if found:
                break
            else:
                print("There is no such data in the file")
        
        # Delete row by name
        delete(name_search, data_list) 
        print()

    # 2. Search Phone Number
    if user_option == 2:

        while True:
            phone_search = input("What phone number do you want to search? ")
            phone_search = format_phone(phone_search)
            found = search_in_table(phone_search, data_list)
            if found:
                break
            else:
                continue

        # Delete row by phone number
        delete(phone_search, data_list) 
        print()

    # 3. Search SSN
    if user_option == 3:

        while True:
            ssn_search = input("What SSN do you want to search? ")
            ssn_search = format_ssn(ssn_search)
            found = search_in_table(ssn_search, data_list)
            if found:
                break
            else:
                continue

        # Delete row by SSN
        delete(ssn_search, data_list) 
        print()
        

    # Return True if user wants to repeat Menu, otherwise No
    while True:
        try:
            menu_choice= input("Do you want to add, update, delete, or search another contact? (Y/N): ")
            if menu_choice[0].upper() == 'Y':
                return True
            elif menu_choice[0].upper() == 'N':
                return False
            else:
                print("\nPlease choose Yes or No. ")
        except ValueError:
            print("\nInvalid answer. Type (Y/N). ")

    
    


# Function to display - Search Entries Menu
def LookEntry():
    print("")
    while True:
        try:    
            print("Search a contact to see his/her INFO")
            print("How would you like to search?")
            print("\t1. Name")
            print("\t2. Phone Number")
            print("\t3. Social Security Number")
            user_option = int(input("Enter a number 1-3: "))
            if user_option >= 1 and user_option <= 3:
                break
            else:
                print("Please enter a number between 1 and 3\n")
        except ValueError:
            print("Wrong input. Please enter a valid integer number\n")

    # 1. Search Name
    if user_option == 1:
        found = False

        while True:
            name_search = input("Which name do you want to search? ")
            name_search = format_name(name_search)
            found = search_in_table(name_search, data_list)
            if found:
                (name, email, phone, ssn) = search_row(name_search, data_list)
                print ("We found a contact...")
                print ("Name:" , name)
                print ("E-mail:" , email)
                print ("Phone Number:" , phone)
                print ("SSN:" , ssn)
                break
            else:
                print("There is no such data in the database")
        

    # 2. Search Phone Number
    if user_option == 2:

        while True:
            phone_search = input("What phone number do you want to search? ")
            phone_search = format_phone(phone_search)
            found = search_in_table(phone_search, data_list)
            if found:
                (name, email, phone, ssn) = search_row(phone_search, data_list)
                print ("\nWe found a contact")
                print ("Name:" , name)
                print ("E-mail:" , email)
                print ("Phone Number:" , phone)
                print ("SSN:" , ssn)
                break
            else:
                continue


    # 3. Search SSN
    if user_option == 3:

        while True:
            ssn_search = input("What SSN do you want to search? ")
            ssn_search = format_ssn(ssn_search)
            found = search_in_table(ssn_search, data_list)
            if found:
                (name, email, phone, ssn) = search_row(ssn_search, data_list)
                print ("\nWe found a contact")
                print ("Name:" , name)
                print ("E-mail:" , email)
                print ("Phone Number:" , phone)
                print ("SSN:" , ssn)
                break
            else:
                continue

    

    # Return True if user wants to repeat Menu, otherwise No
    while True:
        try:
            menu_choice= input("Do you want to add, update, delete, or search another contact? (Y/N): ")
            if menu_choice[0].upper() == 'Y':
                return True
            elif menu_choice[0].upper() == 'N':
                return False
            else:
                print("\nPlease choose Yes or No. ")
        except ValueError:
            print("\nInvalid answer. Type (Y/N). ")




# Function to display - Programmer Info
def programInfo():
    print("\n\nThanks for using this Program")
    print("Author:", "Jose Valdivia Rojas")
    print("Course:", "CMSC 206")
    print("Assignment:", "Project 3B (Address Book)")
    print("© 2022 JOSE VALDIVIA ALL RIGHTS RESERVED")
    exit()


# Main() - Program starts
print("-------------------------WELCOME------------------------")
while True:
    try:
        display = input("Would you like to display a current list of contacts? (Y/N) ")
        if display[0].upper() == 'Y':
            show_table(data_list)
            break
        elif display[0].upper() == 'N':
            break
        else:
            print("Wrong choice. Type Yes or No")
    except ValueError:
        print("Invalid input. Please type Yes or No")

print("")
print("")
while True:
    try:    
        print("\nWhat would you like to do?")
        print("\t1. Add entry")
        print("\t2. Update entry")
        print("\t3. Delete entry")
        print("\t4. Look up an entry")
        print("\t5. Quit")
        user_choice = int(input("Enter a number 1-5: "))
        if user_choice >= 1 or user_choice <= 5:
            if user_choice == 1:
                repeat_menu = addEntry()
                if repeat_menu:
                    continue    # Continue the next loop
                else:
                    break

            elif user_choice == 2:
                repeat_menu = updateEntry()
                if repeat_menu:
                    continue    # Continue the next loop
                else:
                    break

            elif user_choice == 3:
                repeat_menu = deleteEntry()
                if repeat_menu:
                    continue    # Continue the next loop
                else:
                    break

            elif user_choice == 4:
                repeat_menu = LookEntry()
                if repeat_menu:
                    continue    # Continue the next loop
                else:
                    break
            elif user_choice == 5:
                show_table(data_list)
                write_and_close_program(data_list)
                programInfo()
        else:
            print("Please enter a number between 1 and 5\n")
    except ValueError:
        print("Wrong input. Please enter a valid integer number\n")

# Closing Program
close_program = input("Do you want to COMMIT the changes? (Y/N): ")
if close_program[0].upper() == 'Y':
    print("\nThe database is updated...")
    show_table(data_list)
    write_and_close_program(data_list)
    programInfo()
elif close_program[0].upper() == 'N':
    print("\nNo changes to the database were made...")
