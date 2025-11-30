def basit_hesap_makinesi():
    
    try:
        number1 = float(input("enter first number: "))
        number2 = float(input("enter second number: "))
        
        toplam = number1+number2   
        fark = number1 - number2
        carpim = number1 * number2
        
        print("\n--- Outcomes ---")
        print(f"Toplam ({number1} + {number2}): {toplam}")
        print(f"Fark ({number1} - {number2}): {fark}")
        print(f"Çarpim ({number1} * {number2}): {carpim}")
        
        # kontrol
        if number2 != 0:
            bolum = number1 / number2
            print(f"Bölüm ({number1} / {number2}): {bolum}")
        else:
            print("you cannot divide number with 0.")
            
    except ValueError:
        print("error please enter the valid number.")

basit_hesap_makinesi()