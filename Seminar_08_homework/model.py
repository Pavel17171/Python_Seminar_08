import csv
import json

#reader_object = "student_book.csv"

def read_file_csv(x):
    with open(x, encoding = 'utf-8') as r_file:
        data = []
        file_reader = csv.reader(r_file, delimiter = "_")
        for i in file_reader:
            data.append(i)
    return(data)

def export_file(data, name_file):
    data1 = open (name_file, 'w', encoding = 'utf-8')    
    for i in range(len(data)):
        data1.writelines(f'{("_").join(data[i])}\n')
    data1.close()

#4. Добавить студента
def new_student_add(data):
    data.append([])  
    index = len(data)-1
    data[index].append(str(index))    
    data[index].append(input("Введите фамилию: "))
    data[index].append(input("Введите имя: ")) 
    data[index].append(input("Введите отчество: "))  
    data[index].append(input("Введите факультет: ")) 
    data[index].append(input("Введите специальность: ")) 
    data[index].append(input("Введите номер группы: ")) 
    data[index].append(input("Введите номер телефона: ")) 

def save_file_csv(data):
    data1 = open (f'student_book.csv', 'w', encoding = 'utf-8')    
    for i in range(len(data)):
        data1.writelines(f'{("_").join(data[i])}\n')
    data1.close()

#5. Удалить студента
def delete_student(data, temp):
    temp_list = []
    for i in data:
        if temp[0] != i:
            temp_list.append(i)             
    return temp_list

# 6. Экспорт в формате ".txt"
def export_file_txt(data, name_file):
    data1 = open (name_file, 'w', encoding = 'utf-8')    
    for i in range(len(data)):
        data1.writelines(f'{("_").join(data[i])}\n')
    data1.close()

#7. Экспорт в формате ".json"
def for_export_json(data):
    temp = []
    for i in range(1, len(data)):
        temp.append(dict(ID=data[i][0],\
Фамилия=data[i][1],\
Имя=data[i][2],\
Отчество=data[i][3],\
Факультет=data[i][4],\
Специальность=data[i][5],\
Группа=data[i][6],\
Телефон=data[i][7]))
    return temp

def export_file_json(data, name_file):
    data = for_export_json(data)
    with open(name_file, 'w') as page:
        json.dump(data, page)

def save_request(data):
    print("Сохранить изменения?")
    question = input("Нажмите:\nY/Д - да\nN/Н - нет\n").lower()
    if question == 'y'.lower() or question == 'д'.lower():
        save_file_csv(data)
        return False
    elif question == 'n'.lower() or question == 'н'.lower():
        return False
    else:
        print("Введен некорректный ответ")
        save_request(data)