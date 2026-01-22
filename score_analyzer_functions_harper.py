def score_analyzer(number_grade):
    if number_grade >= 90:
        return 'A'
    elif number_grade >= 80:
        return 'B'
    elif number_grade >= 70:
        return "C"
    else:
        return "F"


def list_of_variables(name, number_grade, letter_grade):
    mainList = [name, number_grade, letter_grade]
    print(mainList)
    return [name, number_grade, letter_grade]