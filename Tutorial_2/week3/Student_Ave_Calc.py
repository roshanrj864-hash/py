choice = 'y'

while choice == 'y':
    quiz_1 = float(input("Enter the score for Quiz 1: "))
    quiz_2 = float(input("Enter the score for Quiz 2: "))
    quiz_3 = float(input("Enter the score for Quiz 3: "))


    average = (quiz_1 + quiz_2 + quiz_3) / 3

    if average >= 50:
        print("PASS")
    else:
        print("FAIL")

    choice = input("Continue? (y/n): ")

print("Program Ended")