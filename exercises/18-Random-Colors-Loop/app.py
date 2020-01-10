import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    pancakes={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return pancakes.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    # example_color = 1
    students_array = []
    #your loop here

    for num in range(10):
        num = get_color(random.randint(1,4))
        students_array.append(num)

    return students_array
# print(get_allStudentColors())


print(get_allStudentColors())
