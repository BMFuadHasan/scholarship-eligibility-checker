gpa = float(input("Enter GPA: "))
attendance = float(input("Enter Attendance (%): "))
activities = input("Participated in extracurricular activities? (yes/no): ")
low_income = input("Low-income family? (yes/no): ")
disciplinary = input("Any disciplinary action? (yes/no): ")

if gpa == 4.0:
    print("Qualified (Automatic - GPA 4.0)")
else:
    if attendance < 60:
        print("Disqualified (Attendance below 60%)")
    else:
        if disciplinary == "yes":
            print("Disqualified (Disciplinary action)")
        else:
            if gpa >= 3.5:
                if attendance >= 80:
                    if activities == "yes" or low_income == "yes":
                        print("Qualified for Scholarship")
                    else:
                        print("Not Qualified")
                else:
                    print("Not Qualified")
            else:
                print("Not Qualified")

