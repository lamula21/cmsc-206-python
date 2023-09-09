# Author: Jose A. Valdivia Rojas
# Course: CMSC 206
# Project 1 - Final Submission


 
# Functions
def decimal_to_hex(decimal):
  hex_list = list()
  result = ''

  # Algorithm to convert decimal to hex
  while decimal != 0:
    remainder = decimal % 16
    decimal = decimal // 16
    hex_list.append(remainder)

  hex_list.reverse()      # [list].reverse() to reverse the elements of the list
  
  str_hex_list = [str(x) for x in hex_list]   # Convert the int list to a string list using for loop


  # Find numbers and change to its hexadecimal letters in the list
  for i in range(len(str_hex_list)):
    if str_hex_list[i] == '10':
      str_hex_list[i] = 'A'
    elif str_hex_list[i] == '11':
      str_hex_list[i] = 'B'
    elif str_hex_list[i] == '12':
      str_hex_list[i] = 'C'
    elif str_hex_list[i] == '13':
      str_hex_list[i] = 'D'
    elif str_hex_list[i] == '14':
      str_hex_list[i] = 'E'
    elif str_hex_list[i] == '15':
      str_hex_list[i] = 'F'


  # For loop the whole list to store in a str variable
  for each in str_hex_list:
    result += each + ''

  return result




def decimal_to_oct(decimal):
  oct_list = list()
  result = ''

  # Algorithm to convert decimal to hex
  while decimal != 0:
    remainder = decimal % 8
    decimal = decimal // 8
    oct_list.append(remainder)

  oct_list.reverse()      # [list].reverse() to reverse the elements of the list
  
  str_oct_list = [str(x) for x in oct_list]   # Convert the int list to a string list using for loop


  # For loop the whole list to store in a str variable
  for each in str_oct_list:
    result += each + ''

  return result




def decimal_to_binary(decimal):
  binary_list = list()
  result = ''

  # Algorithm to convert decimal to hex
  while decimal != 0:
    remainder = decimal % 2
    decimal = decimal // 2
    binary_list.append(remainder)

  binary_list.reverse()      # [list].reverse() to reverse the elements of the list
  
  str_binary_list = [str(x) for x in binary_list]   # Convert the int list to a string list using for loop


  # For loop the whole list to store in a str variable
  for each in str_binary_list:
    result += each + ''

  return result




def binary_to_decimal(binary):
  decimal_number = 0
  power = 0   

  # For each digit from right to left
  while binary > 0:
    remainder = binary % 10   # Take the first right digit
    decimal_number += (remainder) * ( 2**power)    # Multiply that digit by 2 to some power
    power += 1      # Power starts from 0 and keeps incrementing by 1
    binary //= 10    # Take the next right digit by dividing it by 10

  return decimal_number




# Menu
# While loop forever until user press exit
while True: 
  print("\n----------------------------------------------------------------")
  print("Number Converter: Convert a number (between 0 and 1024) from ")

  print("\nEnter 1 -- Decimal to Hexadecimal",
  "\nEnter 2 -- Decimal to Octal",
  "\nEnter 3 -- Decimal to Binary (Between 0 and 256)",
  "\nEnter 4 -- Binary to Decimal (only 1 and 0)",
  "\nEnter X -- Exit")

  print("")
  user_choice = -1  # Stores a flag value in the variable, which will be changed when user_choice is entered
  user_input = -1    # Stores a flag value in the variable, which will be changed when user_input is entered


  # While user choice is other than 1, 2, 3, X, loop to prompt the user menu choice
  while user_choice == -1:

    user_choice = input("Enter your choice: ")

    # Exit. If the user input is X or x, exit program
    if user_choice == 'X' or user_choice == 'x':
      print("\nThanks for using Converter Number Program","\nProgram is closing...")
      exit()


    # 1. If the user choice is 1, convert to hexadecimal format
    elif user_choice == '1':                           


      # While loop when user input is out of range
      while user_input <= -1 or user_input >= 1025:

        # try/except to catch error of string text
        try:
          user_input = int(input("\nEnter a decimal number: "))

          if user_input <= -1 or user_input >= 1025:
            print("Please. Choose a number between 0 and 1024\n")
          else: 
            result = decimal_to_hex(user_input)
            # Print the result
            print("Base-10:", user_input, f"\nHex: 0x{result}\n")    # Use the f-print function to print the result
            

        except ValueError:
          print("Could not convert a text. Please enter a number next time\n", "\n--------------------------------------------------------\n")
          user_input = -1   # Set flag to -1 to loop the prompt again




    # 2. If the user choice is 2, convert to octal format
    elif user_choice == '2':                             
      
      # While loop when user input is out of range
      while user_input <= -1 or user_input >= 1025:

        # try/except to catch error of string text
        try:
          user_input = int(input("\nEnter a decimal number: "))

          if user_input <= -1 or user_input >= 1025:
            print("Please. Choose a number between 0 and 1024\n")
          else: 
            result = decimal_to_oct(user_input)
            # Print the result
            print("Base-10:", user_input, f"\nOctal: 0{result}\n")    # Use the f-print function to print the result

        except ValueError:
          print("Could not convert a text. Please enter a number next time\n", "\n--------------------------------------------------------\n")
          user_input = -1   # Set flag to -1 to loop the prompt user input



      
      
    # 3. If the user choice is 3, convert to binary format
    elif user_choice == '3':                             
      
      # try/except to catch error of string text
      try:
        # While loop when user input is out of range
        while user_input <= -1 or user_input >= 257:
          user_input = int(input("\nEnter a decimal number: "))

          if user_input <= -1 or user_input >= 257:
            print("Please. Choose a number between 0 and 256\n")
          else: 
            result = decimal_to_binary(user_input)
            # Print the result
            print("Base-10:", user_input, "\nBinary:", result, "\n") 
      
      except ValueError:      
        print("Could not convert a text. Please enter a number next time\n", "\n--------------------------------------------------------\n")
        user_input = -1   # Set flag to -1 to loop the prompt user input


    # 4. If the user choice is 4, convert binary to decimal format
    elif user_choice == '4':                            
      
      # try/except to catch error of string text
      try:
        # While loop when user input is out of range
        while user_input <= -1:
          user_input = int(input("\nEnter a binary number: "))


          string_user_input = str(user_input)     # Convert user input to a string
          set_user_input = set(string_user_input) # Use set to get rid off repeated numbers
          allowed_numbers = {"0", "1"}            # A set to be compared with


          # Valdiate the binary number
          if set_user_input == allowed_numbers or set_user_input =={"0"} or set_user_input == {"1"}:
            
            result = binary_to_decimal(user_input)
            # Print the result
            print("Binary:", user_input, "\nBase-10:", result, "\n")
            
          else: 
            print("Please. Choose a number with 0s and 1s\n")

      
      except ValueError:      
        print("Could not convert a text. Please enter a number next time\n", "\n--------------------------------------------------------\n")
        user_input = -1   # Set flag to -1 to loop the prompt user input

    # Exception. If the user choice is out of range, prompt to enter menu choice again
    else:
      print("Wrong number, enter a number between 1-4 or X to exit", "\n--------------------------------------------------------\n")




