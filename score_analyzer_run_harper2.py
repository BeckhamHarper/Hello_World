import score_analyzer_functions_harper

number_of_students = int(input("input amount of students please."))
for i in range(number_of_students):
    number_grade = int(input("Please enter a number grade"))
    name = input("Choose a name please.")
    letter_grade = score_analyzer_functions_harper.score_analyzer(number_grade)
    score_analyzer_functions_harper.list_of_variables(name, number_grade, letter_grade)