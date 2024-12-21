# user_input = int(input("Enter a number and this program will print from 1 to n: "))

# Using for loop

# try:
#     for i in range(1, user_input + 1):
#         print(i)
# except Exception as e:
#     print(e)


# Using while loop

# i = 1
# try:
#     while(i <= user_input):
#         print(i)
#         i += 1
# except Exception as e:
#     print(e)



def main():
    try:
        user_input = int(input("Enter Integer number so this program can print from 1 to n: "))
        
        i = 1
        while(i <= user_input):
            print(i, end=" ")
            i += 1
        
    except Exception as e:
        print("Kindly give integer number.")

if __name__ == "__main__":
    main()
