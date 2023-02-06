from model import export_file, new_student_add, save_file_csv, delete_student

def menu():
    print('\n'
        'Введите номер действия:\n\n'
        '1. Показать список студентов\n'
        '2. Поиск студента\n'
        '3. Сделать выборку\n'        
        '4. Добавить студента\n'
        '5. Удалить студента\n'        
        '6. Экспорт в формате ".txt"\n'
        '7. Экспорт в формате ".json"\n'
        '8. Выход\n')
    answer = int(input("Выполняется команда: "))
    return answer

horizont_line= '-' * 128

def table():
    print()
    print(horizont_line)     
    print("| ID \
| Фамилия        \
| Имя            \
| Отчество       \
| Факультет      \
| Специальность            \
| Группа \
| Телефон         |")
    print(horizont_line)     

# Печать строки данных
def table_line(data_line):
    print(f"| {(data_line[0]).rjust(3)}\
| {data_line[1].ljust(15)}\
| {data_line[2].ljust(15)}\
| {data_line[3].ljust(15)}\
| {data_line[4].ljust(15)}\
| {data_line[5].ljust(25)}\
| {data_line[6].ljust(7)}\
| {data_line[7].ljust(15)} |")

# 1. Показать список студентов
def print_list(data):
    table()
    for i in range(1, len(data)):
        table_line(data[i])
        print(horizont_line)

# 2. Поиск студента
def search_student(data):
    name = input("Введите условие поиска: ")
    temp = []
    count = 0
    print("Результат поиска: ")
    table()
    for i in data:
        if name in i:
            temp.append(i)
            table_line(i)
            print(horizont_line)
            count += 1
    print(f"Найдено {count} записей.")
    return temp


# 3. Сделать выборку
def selection(data):
    temp = search_student(data)
    print("Продолжить выбор?\nДа  - Y/Д\nНет - N/Н")
    ans = input().lower()
    #if ans == 'д' or ans == 'y':    
    while ans == 'д' or ans == 'y':
        temp = search_student(temp)
        print("Продолжить выбор?\nДа  - Y/Д\nНет - N/Н")
        ans = input().lower()
    else:
        print("Сделать экспорт выборки?\nДа  - Y/Д\nНет - N/Н")
        ans = input().lower()
        if ans == 'д' or ans == 'y':
            export_file(temp, 'selection_student.csv')


#4. Добавить студента
def new_student(data):
    new_student_add(data)
    print("Добавить ещё студента?\nДа  - Y/Д\nНет - N/Н")
    ans = input().lower()
    while ans == 'д' or ans == 'y':
        new_student_add(data)
        print("Добавить ещё студента?\nДа  - Y/Д\nНет - N/Н")
        ans = input().lower()    
    else:
        save_file_csv(data)


#5. Удалить студента
def delete_line(data):
    temp = search_student(data)
    print("Удалить?\nДа  - Y/Д\nНет - N/Н")
    ans = input().lower()
    if ans == 'д' or ans == 'y':    
        data = delete_student(data, temp)
        save_file_csv(data)
        print_list(data)

