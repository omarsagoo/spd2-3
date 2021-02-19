import math 

def create_grade_list():
    grade_list = []

    # Get the inputs from the user
    number_of_students = int(input('How many students?  '))

    for _ in range(0, number_of_students):
        grade_list.append(int(input('Enter a grade: ')))

    return grade_list

def mean_of_grades(grade_list):
    # Calculate the mean and standard deviation of the grades
    sum_of_grades = 0
    for grade in grade_list:
        sum_of_grades = sum_of_grades + grade

    mean = sum_of_grades / len(grade_list)

    return mean

def standard_deviation_of_grades(grade_list, mean):
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2

    standard_deviation = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation

    return standard_deviation

def print_banner():
    print('****** Grade Statistics ******')

def print_mean(mean):
    print("The mean of the grades is: ", mean)

def print_standard_deviation(standard_deviation):
    print('The populations standard deviation of grades is: ', round(standard_deviation, 3))

def print_end():
    print('****** END ******')

grades = create_grade_list()
print_banner()
mean = mean_of_grades(grades)
print_mean(mean)
sd = standard_deviation_of_grades(mean)
print_standard_deviation(sd)
print_end()