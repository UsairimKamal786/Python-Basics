medical_cause = input("did you have a medical cause Y or N: ")
atten = int(input("enter the attendance of the student: "))

if medical_cause == 'Y':  #checking the condition 1
    print("You are allowed")
else:
    if atten >= 75:  #checking the condition 2
        print("Allowed")
    else:
        print("Not allowed")
