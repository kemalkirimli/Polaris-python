from datetime import datetime

exam_input = input("Enter your exam date and time (YYYY-MM-DD HH:MM): ")

try:
    exam_date = datetime.strptime(exam_input, "%Y-%m-%d %H:%M")
    now = datetime.now()

    if exam_date < now:
        print("This exam date has already passed.")
    else:
        remaining_time = exam_date - now
        days = remaining_time.days
        hours = remaining_time.seconds // 3600

        print(f"Time left until your exam:")
        print(f"{days} days")
        print(f"{hours} hours")

except ValueError:
    print(" Please enter the date in the correct format: YYYY-MM-DD HH:MM")
