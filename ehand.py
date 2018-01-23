def add_demo():
    try:
        num1 = input("Input an number : ")
        num1 = int(num1)
        num2 = input("Input an number : ")
        num2 = int(num2)
        sum_num = num1 + num2
    except TypeError:
        print("Please input a number")
    else:
        print('The sum of the input number is : '+ str(sum_num))
    
add_demo()
