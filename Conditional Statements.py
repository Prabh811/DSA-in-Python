# Topic: Conditional Statements (if-else)
# Question 2: Write a Python program that:

# Takes an integer input from the user.
# Checks whether the number is:
# Positive
# Negative
# Zero
# Prints an appropriate message based on the input.


flag = True

while flag:
    
    try:
        number = int(input("Give a number and this program will tell you whether it's a positive, negative or zero: "))
        
        if number > 0:
            print("Number is positive: ")
        
        elif number < 0:
            print("Number is Negative")
            
        else:
            print("Number is Zero")
            
        exit_choice = int(input("If you want this program to exit then type 0: "))
        
        if exit_choice == 0:
            flag = False
              
    except Exception as e:
        print("The Error is: ", e)
        
        
print("You've exited from the program successfully")
    
    