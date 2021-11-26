# student_points = {"Angela": 85,
#                   "Bryan": 70,
#                   "Liz": 50,}
# student_rank = {}
# for student in student_points:
#     points = student_points[student]
#     if points >= 84:
#         student_points[student] = "Best"
#     elif points >= 70:
#         student_points[student] = "Better"
#     elif points == 50:
#         student_points[student] = "worst"
#         student_rank = student_points
# print(student_rank)


# function with outputs
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f" Result {formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("what is your first name"),input("what is your last name")))
#
#
#

# Quiz
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# print(add(2, multiply(5, divide(8, 4))))

# def my_function(a, b):
#     return a * b
#
#
# print(my_function(a=5, b=3))

# def full_name(first_name, last_name):
#     if first_name == "" and last_name == "":
#         return
#     first = first_name.title()
#     last = last_name.title()
#     tara = f"Your complete name is {first} {last}"
#     return tara
#
#
# print(full_name(input("what is your first name ?\n"), input("what is your last name ?\n")))
#
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"Total {days} days")

