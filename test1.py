from graphi import *

# Variabel to use as rule to while loop
true = True

# defining funtion for validate user input
def validate_user_input():
    while true:

        # making varibale as global varibales
        global pass_value
        global defer_value
        global fail_value

        # creating list to valide user inputs are this list
        list_for_validate = [0,20,40,60,80,100,120]
        try :
            # getting user data

            pass_value = int(input("Please enter your credits at pass : "))
            
            # validating is user's data are in range

            if pass_value in list_for_validate:
                pass
            else:
                print("Out of range.")
                continue
            
            defer_value = int(input("Please enter your credit at defer : "))

            if defer_value in list_for_validate:
                pass
            else:
                print("Out of range.")
                continue
            
            fail_value = int(input("Please enter your credit at fail : "))

            if fail_value in list_for_validate:
                pass
            else:
                print("Out of range.")
                continue

        except ValueError :
            print("Integer required")
            continue
        else:
            # total variable for validate total user input are in range 
            total = pass_value + defer_value + fail_value
            
            if total == 120:
                break
            else:
                print("Total incorrect.")
                continue
                
    # print(total)
    # print(pass_value)
    # print(defer_value)
    # print(fail_value)

    return pass_value,defer_value,fail_value

# to predict progression outcomes
def progression_outcomes():
        
         # making varibale as global varibales
        global progress
        global trailer
        global retriever
        global excluded

        if pass_value == 120:
            print("Progress")

            progress += 1

        elif pass_value == 100:
            print("Progress (module trailer)")

            trailer += 1

        elif fail_value <= 60:
            print("Do not progress – module retriever")

            retriever += 1

        else:
            print("Exclude")

            excluded += 1

#decision validating
def decision_validate():
    true = True
    global decision
    while true:
        decision = str(input("Enter 'y' for yes or 'q' to quit and view results : "))
        if decision.lower() == "q" or decision.lower() == "y":
            true = False
        else:
            print("Enter valide input")
            
    return decision

#programe starting
progress = 0
trailer = 0 
retriever = 0
excluded = 0
while true:  
    #calling user defined functions       
    validate_user_input()
    progression_outcomes()

    print("Would you like to enter another set of data?")
    decision_validate()
    if decision.lower() == 'q':
        print("exiting")
        true = False
    else:
        continue
else:
    print("The program should now display a histogram of results using the graphics.py module")
    list = [progress,trailer,retriever,excluded]
    print(list)
    histogram(progress,trailer,retriever,excluded)
    