# Dahan, Regine Fae M. BSCPE 1-5 ( Simple Calculator: Exception Handling )

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
            the_sum = A_Addition(num_1, num_2)  

        #print sum
            print(" The sum of two numbers is >>> ", the_sum)

    #if subtraction
        if user_choice == "S":
            the_diff = S_Subtraction(num_1, num_2)

        #print difference
            print(" The difference of two numbers is >>> ", the_diff)

    #if multiplication
        if user_choice == "M":
            the_prod = M_Multiplication(num_1, num_2)

        #print product
            print(" The product of two numbers is >>> ", the_prod)

    #if division
        if user_choice == "D":
            the_quo = D_Division(num_1, num_2)

        #print quotient
        print(" The quotient of two numbers is >>> ", the_quo)


#note: do not forget to add exception handling