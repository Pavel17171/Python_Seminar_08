from view import menu, print_list, search_student, selection, new_student, delete_line
from model import read_file_csv, export_file_txt, export_file_json, save_request


def button_click():
    reader_object = 'student_book.csv'

    answer = menu()
    while (answer != 0):
        students_list = read_file_csv(reader_object)
        if answer == 1:
            print_list(students_list)
        elif answer == 2:
            search_student(students_list)
        elif answer == 3:
            selection(students_list)
        elif answer == 4:
            new_student(students_list)
        elif answer == 5:
            students_list = delete_line(students_list)       
        elif answer == 6:
            export_file_txt(students_list, 'student_book.txt')
        elif answer == 7:
            export_file_json(students_list, 'student_book.json')
        elif answer == 8:
            save_request(students_list)
            break

        answer = menu()