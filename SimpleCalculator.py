# Dahan, Regine Fae M. BSCPE 1-5 ( Simple Calculator: Exception Handling )

#introduction
import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()
print(Fore.BLACK+pyfiglet.figlet_format("CALCULATOR",font="stop"))
time.sleep(1)
border = "✪" * 75
border_2 = " 𓇼 " * 25
print(border)
print(Fore.LIGHTBLUE_EX+' THIS PROGRAM WILL HELP YOU ADD, SUBTRACT, MULTIPLY or DIVIDE TWO NUMBERS... ')
print(border)
time.sleep(2)

run_count = 0
def main():

    global run_count
    run_count = run_count +1 
    try:

        #each operation's calculation
        def addition(num_1, num_2):
            return num_1 + num_2

        def subtraction(num_1, num_2):
            return num_1 - num_2

        def multiplication(num_1, num_2):
            return num_1 * num_2

        def division(num_1, num_2):
            return num_1 / num_2
            
        #user choosing the operation
        while True:
            print (Fore.LIGHTMAGENTA_EX+ " CHOOSE YOUR DESIRED OPERATION.\n If Addition, press A.\n If Subtraction, press S.\n If Multiplication, press M.\n If Division, press D. ")
            user_choice = input(" >>> ").upper()

            if user_choice in ["A", "S", "M", "D"]:
                print(border_2)
                num_1 = float(input(Fore.YELLOW+ " Enter your first number: "))
                num_2 = float(input(Fore.GREEN+ " Enter your second number: "))
                print(border_2)

            #if addition
                if user_choice == "A":
                    the_result = addition(num_1, num_2)  
                    print(Fore.WHITE+pyfiglet.figlet_format("Computing...",font="wavy"))
                    time.sleep(4)
                #print sum
                    print(Fore.BLUE+" The SUM of two numbers is >>> ", the_result)
                    print(border)
                
            #if subtraction
                elif user_choice == "S":
                    the_result = subtraction(num_1, num_2)
                    print(Fore.WHITE+pyfiglet.figlet_format("Computing...",font="wavy"))
                    time.sleep(4)

                #print difference
                    print(Fore.BLUE+" The DIFFERENCE of two numbers is >>> ", the_result)
                    print(border)

            #if multiplication
                elif user_choice == "M":
                    the_result = multiplication(num_1, num_2)
                    print(Fore.WHITE+pyfiglet.figlet_format("Computing...",font="wavy"))
                    time.sleep(4)

                #print product
                    print(Fore.BLUE+" The PRODUCT of two numbers is >>> ", the_result)
                    print(border)

            #if division
                elif user_choice == "D":
                    the_result = division(num_1, num_2)
                    print(Fore.WHITE+pyfiglet.figlet_format("Computing...",font="wavy"))
                    time.sleep(4)
                    
                #print quotient
                    print(Fore.BLUE+" The QUOTIENT of two numbers is >>> ", the_result)
                    print(border)
                
                break
            else: 
                print (" Invalid. ")
    
    
    except ValueError: 
        print (Fore.RED+" ERROR: Make sure you input a number instead of words. ")
    except TypeError:
        print (Fore.RED+" ERROR: Make sure your input is correct. ")
    except ZeroDivisionError:
        print (Fore.RED+" ERROR: You cannot divide by 0. ")    
    finally:
        print (Fore.MAGENTA+" Hey, don't forget to smile ; ) ")

#try again?
while True:
    if run_count != 0:
        try_again = input (Fore.BLUE+' PRESS 1 if you want to try again. PRESS 2 if otherwise. ')
    else: 
        try_again = input (Fore.LIGHTBLACK_EX+' PRESS 1 to START. ')
        print(border_2)

    if (try_again == '1'):
        main()
    elif (try_again == '2'):
        print(border)
        print(Fore.BLACK+pyfiglet.figlet_format("THANK YOU!",font="utopia"))
        exit()
    else:
        print('Invalid.')
