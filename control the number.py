def control_Negative_or_positive():

    try:
        number = float(input("enter the number: "))
        
        if number > 0:
            result = "Positive"
        elif number < 0:
            result = "Negative"
        else:
            result = "zero"
            
        print(f"({number}) is {result}.")
        
    except ValueError:
        print("erorr: enter the valid number.")

control_Negative_or_positive()