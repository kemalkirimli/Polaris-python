def calculaterofscore():
    
    score = 50
    yourScore= int(input("Enter the your score: "))
    if yourScore >= score:
            print(f"your score: {yourScore}. result: **passed**.")
    else:
            print(f"your score: {yourScore}. result:  **failed**.")
            
        
calculaterofscore()
