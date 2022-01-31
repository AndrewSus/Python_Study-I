# # 1.	Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.


# Определим список для ввода данных
# Откроем файл для записи (если его нет - создаётся)
# Определим цикл для ввода данных - условие завершения - пустая строка
# Заполняем данными
# Вариант 1
abc = input(" Вводим данные")
with open("one_file.txt", "w+", encoding='utf-8') as one_file:
    while abc:
        one_file.write(abc+'\n')
        abc = input("Вводим следующую сроку: ")

# Вариант 2
abc = input(" Вводим данные")
file_obj = open("one_file.txt", "w+", encoding='utf-8')
while abc:
    file_obj.writelines(abc+'\n')
    abc = input("Вводим следующую сроку: ")


file_obj.close()

# Вариант 3 запись в файл через print()

abc = input(" Вводим данные")
file_obj = open("one_file.txt", "w+", encoding='utf-8')
while abc:
    print(abc+'\n', file=file_obj)
    abc = input("Вводим следующую сроку: ")


file_obj.close()



# #2.	Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.
file_obj = open("two_file.txt", encoding='utf-8')
file_obj_lines = file_obj.readlines()
print("количество строк в файле: ", len(file_obj_lines))
for file_obj_lines, line in enumerate(file_obj_lines, 1):
   print(f"Количество слов (в строке) {file_obj_lines}: ", len(line.split()))
file_obj.close()



# 3.	Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

itog = 0
file_obj = open("tree_file.txt", encoding='utf-8')
file_obj_lines = file_obj.readlines()
for line in file_obj_lines:
    family_name, oklad = line.split()
    itog += int(oklad)
    if int(oklad) < 20000:
        print(f'{family_name}:  Оклад менее 20 000 руб.')
print("Средний доход по организации: ", itog/len(file_obj_lines))

file_obj.close()


# 4.	Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

# Создадим файл
# Внутри скрипта создадим словарь соответствия английстких и русских слов
# Открываем файл на чтение
# Открываем/создаём файл на запись
# проходим циклом по строка - убираем до числительного
# записываем в файл текстовую строку из словая и добавляем числительное из прочтенного файла
# Посмотрим результаты в созданном файле

perevod = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть",
           "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}
file_obj = open("Four_file.txt", encoding='utf-8')
file_obj_write = open("Four_file_1.txt", "w+", encoding='utf-8')
#file_obj_write = open("Four_file_1.txt", "x", encoding='utf-8')
for line in file_obj.readlines():
    text_nom, nom = line.rstrip().split(' - ')
    file_obj_write.write(f'{perevod[text_nom]} это {nom}\n')
file_obj.close()
file_obj_write.close()


# 5.	Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить её на экран.

file_obj = open("Five_file.txt", "w+", encoding='utf-8')
input_numbers = input("Вводим числа через пробел ....")
file_obj.write(input_numbers)
file_obj.close()

file_obj = open("Five_file.txt", "r", encoding='utf-8')
content = file_obj.read().rstrip().split()
print(content, "- Это в файле")
content_list = [int(el) for el in content if el.isdigit()]
print(content_list, "- Это то, что было числами")
print(sum(content_list), " - Это сумма чисел")
file_obj.close()




# 6.	Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# Создаём файл. Содержимое из примера строк
# Создаём словарь
# обрабатываем данные из файла и записываем в словарь

result_dict = {}
#with open("Six_file.txt", encoding='utf-8') as file:
file = open("Six_file.txt", "w+", encoding='utf-8')
for line in file:
    lesson_type, *lessons = line.split()
    lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson !='—']
    result_dict.update({lesson_type.rstrip(":"): sum(lesson_count)})
print(result_dict)
file.close()

# 7.	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

result_list = [] #Результирующий список
dict_plus_profit = {} #Словарь фирм с прибылью
dict_minus_profit = {} #Словарь фирм с убытком
average_profit_list = [] #Список со средней прибылью - для расчёта
#file = open("Seven_file.txt", encoding='utf-8')
with open("Seven_file.txt", encoding='utf-8') as file:
    #average_profit_list = []
    for line in file.readlines():
        name, _, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profit_list.append(profit)
            dict_plus_profit.update({name: profit})
        else:
            dict_minus_profit.update({name: profit})
    result_list.append(dict_plus_profit)
    result_list.append(dict_minus_profit)
    result_list.append({"average_profit": sum(average_profit_list)/len(average_profit_list)})
#file.close()
with open("Seven_file.json", "w+") as file_obj:
    #file = open("Seven_file.json", "w+", encoding='utf-8')
    json.dump(result_list, file_obj)
#file.close()
