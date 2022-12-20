# 1. Задача про суп:
class Soup:
    def __init__(self, main_ingredient=''):
        self.main_ingredient = main_ingredient

    def show_my_soup(self):
        if self.main_ingredient == '':
            print('Это обычный кипяток!')
        else:
            print(f'Суп --- {self.main_ingredient}')


hot_water = Soup()
hot_water.show_my_soup()

borsch = Soup('свекла')
borsch.show_my_soup()


# 2. Задача про студентов.


class Student:
    def __init__(self):
        self.name = ''
        self.group = ''
        self.progress = []


stud_1 = Student()
stud_2 = Student()
stud_3 = Student()
stud_4 = Student()
stud_5 = Student()

stud_1.name = 'Andrew'
stud_2.name = 'Vjatscheslav'
stud_3.name = 'Cyrill'
stud_4.name = 'Dick'
stud_5.name = 'Artem'

stud_1.group = 1
stud_2.group = 1
stud_3.group = 2
stud_4.group = 3
stud_5.group = 3

stud_1.progress = [5, 5, 4, 5, 4]
stud_2.progress = [5, 5, 5, 5, 4]
stud_3.progress = [3, 5, 4, 5, 4]
stud_4.progress = [5, 3, 3, 3, 4]
stud_5.progress = [5, 5, 5, 5, 3]

students_list = [stud_1, stud_2, stud_3, stud_4, stud_5]


def students(list_of_students):
    new_list = []
    avg_progress_list = []
    students_with_grades = []
    # min_1, min_2, min_3 = 0
    help_lst = []
    # сортированный по имени список студентов
    for i in range(len(list_of_students)):
        new_list.append(list_of_students[i].name)
    new_list = sorted(new_list)
    print('Сортированный по имени список студентов: ')
    for i in range(len(new_list)):
        print(new_list[i])

    # оценки

    for i in range(len(list_of_students)):
        avg_progress_list.append(sum(list_of_students[i].progress) / len(list_of_students[i].progress))
        students_with_grades.append(list_of_students[i].name + '---' + str(avg_progress_list[i]))

    for i in range(len(students_with_grades)):
        help_lst.append(students_with_grades[i].split('---'))
        help_lst[i][0], help_lst[i][1] = help_lst[i][1], help_lst[i][0]
        help_lst = sorted(help_lst)
    print(f'3 Студента с наихудшей успеваемостью (ср.балл - имя):\n {help_lst[0]} \n {help_lst[1]} \n {help_lst[2]}')


students(students_list)
