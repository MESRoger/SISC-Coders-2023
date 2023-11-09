def main():
    numeric_grade = int(input("What's your grade? "))
    letter_grade = convert_to_letter(numeric_grade)
    print(letter_grade)

def convert_to_letter(grade):
    if grade > 95 and grade <= 100:
        return 'VS'
    elif grade > 90:
        return 'S'
    elif grade > 85:
        return 'AA'
    elif grade >= 80:
        return 'A'
    elif grade >= 70:
        return 'LA'
    elif grade >= 0 and grade < 70:
        return 'P'
    else:
        return 'Please type valid grades'

main()