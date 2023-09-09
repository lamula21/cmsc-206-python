# Author: Jose A. Valdivia Rojas
# Course: CMSC 206
# Project 2 - Final Submission


# CONSTANTS DATA
import math

# Constants
BURGERS_PER_PACK_COST = 18
BURGERS_PER_PACK=12

CHCK_PATTIES_PER_PACK_COST=8
CHCK_PATTIES_PER_PACK=4

BUN_PER_PACK_COST=6
BUN_PER_PACK=12

SALAD_BAG_COST = 5
SALAD_BAG = 10

CHIPS_BAG_COST=12
CHIPS_BAG=24

SOFTDRINK_CANS = 12
SOFTDRINK_CANS_COST = 4

HOST_CHARGE_PER_HOUR = 20

# Initialize variables
burgers_per_person = 0
chck_sandwich_per_person = 0
salad_per_person = 0

# Welcome
print("Welcome to McJose's Burgers! Let's estimate your cookout cost.")
customer_name = input("What is your name? ")

while True:

    try:
        number_guest = int(input(f"Welcome {customer_name}, How many guests will be attending the cookout? "))        # F-string to print name into built-in input function
        if number_guest < 1:
            print("Please enter number of guests. Minimum people is one guest")
        else:
            break
    except ValueError:
        print("Please enter a valid number")
        

  

# Serve burgers
serve_burgers = input("Would you like us to serve burgers? Y/N ").upper()
while serve_burgers != "Y" or serve_burgers != "N":
    if serve_burgers == "Y":
        print("Great, we'll serve burgers!")

        while True:
            try:
                burgers_per_person = int(input("How many burgers do you think each person will eat? "))
                break
            except ValueError:
                print("Please re-enter a valid number")
        break

    elif serve_burgers == "N":
        break
    else:
        serve_burgers = input("Please enter Y for yes or N for no: ").upper()

# Serve chicken sandwich
serve_chck_sandwich = input("Would you like us to serve chicken sandwich? Y/N ").upper()
while serve_chck_sandwich != "Y" or serve_chck_sandwich != "N":
    if serve_chck_sandwich == "Y":
        print("Great, we'll serve chicken sandwich!")

        while True:
            try:
                chck_sandwich_per_person = int(input("How many chicken sandwich do you think each person will eat? "))
                break
            except ValueError:
                print("Please re-enter a valid number")
        break

    elif serve_chck_sandwich == "N":
        break
    else:
        serve_chck_sandwich = input("Please enter Y for yes or N for no: ").upper()

# Serve salads
serve_salad = input("Would you like us to serve salad? Y/N ").upper()
while serve_salad != "Y" or serve_salad != "N":
    if serve_salad == "Y":
        print("Great, we'll serve salads!")

        while True:
            try:
                salad_per_person = int(input("How many bowls of salads do you think each person will eat? "))
                break
            except ValueError:
                print("Please re-enter a valid number")
        break

    elif serve_salad == "N":
        break
    else:
        serve_salad = input("Please enter Y for yes or N for no: ").upper()

# Meals Option
while True:
    meals = input("Would you like chips and drink for each customer Y or N ").upper()
    if meals.upper() == 'Y':
        meals = 3
        break
    elif meals.upper() == 'N':
        meals = 0
        break
    else:
        print("Please enter Y for yes or N for no: ")


# Host Calculation
while True:
    try:
        party_time = int(input("How long will the party last, in hours? "))
        if party_time >= 3:
            host_cost = party_time * HOST_CHARGE_PER_HOUR
            break
        else:
            print("The minimum time for host a party is three hours. Please re-enter.")
    except ValueError:
        print("Please re-enter a valid number")

    

# Coupon code
while True:
    coupon_code = input("If you have a coupon code, enter it here. If you don't, press Enter to continue: ")
    if coupon_code.upper() == "JOSE-COUPON":
        coupon_code = 5.00
        break
    elif coupon_code == "":
        coupon_code = 0.00
        break
    else:
        print("Please. Enter a valid coupon code")

# Calculation for minimum packages needed
min_burgers_packages_needed = math.ceil( (number_guest*burgers_per_person) / BURGERS_PER_PACK)
min_chck_sandwich_packages_needed = math.ceil( (number_guest*chck_sandwich_per_person) /  CHCK_PATTIES_PER_PACK)
min_buns_packages_needed = math.ceil( (number_guest*burgers_per_person + number_guest*chck_sandwich_per_person) / BUN_PER_PACK)
min_salad_packages_needed = math.ceil( number_guest*salad_per_person / SALAD_BAG)

min_chips_bags_needed = math.ceil( number_guest / CHIPS_BAG)
min_sodas_cans_needed = math.ceil( number_guest / SOFTDRINK_CANS)



# Calculation for number of leftover 
num_leftover_burgers = (min_burgers_packages_needed * BURGERS_PER_PACK) - (number_guest*burgers_per_person)
num_leftover_chck_patties = (min_chck_sandwich_packages_needed * CHCK_PATTIES_PER_PACK) - (number_guest*chck_sandwich_per_person)
num_leftover_buns = (min_buns_packages_needed * BUN_PER_PACK) - (number_guest*burgers_per_person + number_guest*chck_sandwich_per_person)
num_leftover_chips_bags = (min_chips_bags_needed * CHIPS_BAG) - (number_guest * 1)
num_leftover_soda_cans = ( min_sodas_cans_needed * SOFTDRINK_CANS) - (number_guest * 1)
num_leftover_salad_packages = (min_salad_packages_needed*SALAD_BAG) -(number_guest * salad_per_person)




out_of_pocket = (min_burgers_packages_needed * BURGERS_PER_PACK_COST) + (min_chck_sandwich_packages_needed*CHCK_PATTIES_PER_PACK_COST) + (min_buns_packages_needed*BUN_PER_PACK_COST) + (min_salad_packages_needed*SALAD_BAG_COST)
out_of_pocket += (min_chips_bags_needed*CHIPS_BAG_COST) + (min_sodas_cans_needed*SOFTDRINK_CANS_COST) + meals
profit_margin = .2 * out_of_pocket
catering_cost = out_of_pocket + profit_margin + host_cost

# Second part of the program
print("-------------------------------------TOTALS-------------------------------------")

print("Minimum packages of burgers:", min_burgers_packages_needed)
print("Minimum packages of chicken sandwich:", min_chck_sandwich_packages_needed)
print("Minimum packages of buns:", min_buns_packages_needed)
print("Minimum packages of salad:", min_salad_packages_needed)
print("Minimum box of chips:", min_chips_bags_needed)
print("Minimum pack of sodas:", min_sodas_cans_needed)
print(f"Leftovers: {num_leftover_burgers} burgers, {num_leftover_chck_patties} chicken patties, {num_leftover_buns} buns, {num_leftover_salad_packages} salad packages\n{num_leftover_chips_bags} chip bags, {num_leftover_soda_cans} soda cans")
print(f"Out of pocket cost: ${out_of_pocket:.2f}")
print(f"Your host cost: ${host_cost:.2f}")
print(f"Your subtotal: ${catering_cost:.2f}")
print(f"Your discount: ${coupon_code:.2f}")
print(f"TOTAL COST: ${(catering_cost - coupon_code):.2f}")
