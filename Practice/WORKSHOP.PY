# Let's create a calculator using case condition
print("Welcome to calculator")
a = int(input("Enter the num1: "))
b = int(input("Enter the num2: "))

print ("select one operation")
print(" 1 >> addition \n 2 >> substraction \n 3 >> multiplaction \n 4 >> division")
s_value = int (input("Enter operation code: "))

match s_value:
    case 1:
        print("The addition of num: ",a+b)

    case 2:
        print("The substraction of num: ",a-b)
    
    case 3:
        print("The multiplaction of num: ",a*b)
    
    case 4:
        print("The division of num: ",a/b)

