while True:
    try:
        number= int(input("enter the number: "))
        break  
    except ValueError:
        print("please! enter the valid value")

print(f"your number:{number}")
