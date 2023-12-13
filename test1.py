from histrogram import *

# Variabel to use as rule to while loop
true = True

# defining funtion for validate user input
def validate_user_input():
    # making varibale as global varibales
    global pass_value
    global defer_value
    global fail_value
    while true:
        # getting user data
        while true:
            try:
                pass_value = int(input("Please enter your credits at pass : "))            
                # validating is user's data are in range
                if pass_value in range(0,121,20):
                    break
                else:
                    print("Out of range.")
                    continue
            except ValueError:
                    print("Integer required")
                    continue
        while true:
            try:
                defer_value = int(input("Please enter your credit at defer : "))
                if defer_value in range(0,121,20):
                    break
                else:
                    print("Out of range.")
                    continue
            except ValueError:
                    print("Integer required")
                    continue
        while true:
            try:
                fail_value = int(input("Please enter your credit at fail : "))
                if fail_value in range(0,121,20):
                    break
                else:
                    print("Out of range.")
                    continue
            except ValueError:
                print("Integer required")
                continue

#validate total user input are in range 
        if pass_value + defer_value + fail_value == 120:
            break
        else:
            print("Total incorrect.")
            continue
                
    return pass_value,defer_value,fail_value

# to predict progression outcomes , creating relavent list and , counting progress
def progression_outcomes():
        
    # making varibale as global varibales
    global progress
    global trailer
    global retriever
    global excluded

    if pass_value == 120:
        print("Progress")
        tuple = (pass_value,defer_value,fail_value)
        progress_list.append(tuple)
        progress += 1

    elif pass_value == 100:
        print("Progress (module trailer)")
        tuple = (pass_value,defer_value,fail_value)
        trailer_list.append(tuple)
        trailer += 1

    elif fail_value <= 60:
        print("Do not progress – module retriever")
        tuple = (pass_value,defer_value,fail_value)
        retriever_list.append(tuple)
        retriever += 1

    else:
        print("Exclude")
        tuple = (pass_value,defer_value,fail_value)
        excluded_list.append(tuple)
        excluded += 1
    
    return progress_list

#decision validating
def decision_validate():
    global decision
    while true:
        decision = str(input("Enter 'y' for yes or 'q' to quit and view results : "))
        if decision.lower() == "q" or decision.lower() == "y":
            break
        else:
            print("Enter valide input")
            
    return decision

#iterating list and print lists' element
def list_iterate():
    for i in progress_list:
        print(f"progress : {i[0]},{i[1]},{i[2]}")
    for i in trailer_list :
        print(f"Progress (module trailer) : {i[0]},{i[1]},{i[2]}")
    for i in retriever_list:
        print(f"Module retriever : {i[0]},{i[1]},{i[2]}")
    for i in excluded_list:
        print(f"Excluder : {i[0]},{i[1]},{i[2]}")

#writing data to text file 
def writing_file():
    with open('part3.txt','a') as file:
        for i in progress_list:
         file.write(f"progress : {i[0]},{i[1]},{i[2]}\n")
        for i in trailer_list :
            file.write(f"Progress (module trailer) : {i[0]},{i[1]},{i[2]}\n")
        for i in retriever_list:
            file.write(f"Module retriever : {i[0]},{i[1]},{i[2]}\n")
        for i in excluded_list:
           file.write(f"Excluder : {i[0]},{i[1]},{i[2]}\n")

progress = 0
trailer = 0 
retriever = 0
excluded = 0

#list for progression outcomes
progress_list = []
trailer_list = []
retriever_list = []
excluded_list = []

#programe starting

while true:  
    print("Enter 'y' for student or 'q' to teacher and view results : ")
    choice = input("Enter your choice : ")
    if choice.lower() == "y":
        validate_user_input()
        progression_outcomes()
        break
    elif choice.lower() == "q": 
        while true:     
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
        print("Invalid input")
        continue
else:
    print("The program should now display a histogram of results using the graphics.py module")
    try:
        histogram(progress,trailer,retriever,excluded)
    except GraphicsError:
        print("graphic window closing")
    else:
        print("graphic window closing")
    list_iterate()
    writing_file()
    
    