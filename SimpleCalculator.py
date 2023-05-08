# Dahan, Regine Fae M. BSCPE 1-5 ( Simple Calculator: Exception Handling )

def main():

    #introducing the operations
    print ( " You may choose your desired Operation!\n A. Addition\n S. Subtraction\n M. Multiplication\n D. Division ")

    #each operation's calculation
    def A_Addition(num_1, num_2):
        return num_1 + num_2

    def S_Subtraction(num_1, num_2):
        return num_1 - num_2

    def M_Multiplication(num_1, num_2):
        return num_1 * num_2

    def D_Division(num_1, num_2):
        return num_1 / num_2

    #user choosing the operation
    while True:
        print ( " Choose your desired operation.\n If Addition, press A. If Subtraction, press S. If Multiplication, press M. If Division, press D. ")
        user_choice = input(" >>> ").upper()

        if user_choice in ["A", "S", "M", "D"]:
            num_1 = float(input( " Enter your first number: "))
            num_2 = float(input( " Enter your second number: "))

        #if addition
            if user_choice == "A":
                the_result = A_Addition(num_1, num_2)  

            #print sum
                print(" The sum of two numbers is >>> ", the_result)
            
        #if subtraction
            elif user_choice == "S":
                the_result = S_Subtraction(num_1, num_2)

            #print difference
                print(" The difference of two numbers is >>> ", the_result)

        #if multiplication
            elif user_choice == "M":
                the_result = M_Multiplication(num_1, num_2)

            #print product
                print(" The product of two numbers is >>> ", the_result)

        #if division
            elif user_choice == "D":
                the_result = D_Division(num_1, num_2)

            #print quotient
                print(" The quotient of two numbers is >>> ", the_result)
            
            break
        else: 
            print (" Invalid. ")

    #try again?
    while True:
        try_again = input (' PRESS 1 if you want to try again. PRESS 2 if otherwise. ')

        if (try_again == '1'):
            main()
        elif (try_again == '2'):
            print(' Thank you for using my program : ) ')
            exit()
        else:
            print('Invalid.')

main()

#note: do not forget to add exception handling