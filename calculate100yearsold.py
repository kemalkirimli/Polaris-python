import datetime

def yuz_yas_hesapla():
    try:
        name = input("enter the your name: ")
        age = int(input("enter the your age: "))
        
        # Geçerli yılı bulma
        currentYear = datetime.datetime.now().year
        
        # 100 yaşına gireceği yılı hesaplama
        yearOf_100age= currentYear + (100 - age)
        
        print(f"\nhello {name}! you will turn 100 years old in the {yearOf_100age}.")
    
    except ValueError:
        print("error,pleas enter the valid age.")
yuz_yas_hesapla()



