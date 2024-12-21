user_input = int(input("Enter a number and this program will print from 1 to n: "))

try:
    for i in range(1, user_input + 1):
        print(i)
except Exception as e:
    print(e)