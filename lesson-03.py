# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

# пробовал сам:
def test(a, b):
    if b = 0:
        return print("Деление на 0! - ошибка")
    if a or b type <> int:
        return print("Некорректные входные данные!")
    return print(a/b)
a = int(input("Введите число от 0 до 9"))
b = int(input("Введите число от 0 до 9"))
val = test()

def test(a, b):
    if b == 0:
        return print("Деление на 0! - ошибка")
    try:
    except TypeError:
        return "Некорректные входные данные!"
    #return a/b
    return a, b
a = int(input("Введите число от 0 до 9"))
b = int(input("Введите число от 0 до 9"))
print(test(a, b))

# Сам не справился, только с подсказки преподавателя:

def test(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Только не 0 !!!"
    except TypeError:
        return "Другой тип данных"

print(test(int(input()), int(input())))

# print(test(int(input()), int(input())))
# 5
# 0
# Только не 0 !!!


# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

# Создаём словарь для использования:
# personal_arr = {'name': "Пётр", 'surname':"Петров", 'email':"pp@google.com", 'tel': "333-2438-52328",
#                 'borth_year': "1986", 'city': "Москва"}
# print(personal_arr)

def personal_data(**kwargs):
    return f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, E-mail: {kwargs['email']}"

#print(personal_data(name="Пётр", surname="Петров", email="pp@google.com", tel="333-2438-52328", borth_year="1986", city="Москва"))

print(personal_data(name='Пётр', surname= 'Петров', email= 'pp@google.com', tel= '333-2438-52328', borth_year= '1986', city= 'Москва'))



# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    return sum(my_list[:2])

print(my_func(5, 3, 7))

# print(my_func(5, 3, 7))
# 12


# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа
# x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    if y > 0:
        return
    elif y == 1:
        return 1
    elif x<=0:
        return
    else:
        x_pow_y = 1
        while y<0:
            x_pow_y *= 1/x
            y += 1
        return x_pow_y

result = my_func(2, -5)
print(result)





# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых
# чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

def sum_calc(input_str):
    input_list = input_str.split()
    summ = 0
    for el in input_list:
        if el:
            try:
                if el == "N" or el == "No" or el == "q":
                    return summ, False
                else:
                    summ += int(el)
            except ValueError:
                continue
    return summ, True
continue_flag = True
summa = 0
while continue_flag:
    input_str = input("Вводим через пробел числа. Для оставновки введите N или No или q ")
    current_sum, continue_flag = sum_calc(input_str)
    summa += current_sum
    print("Промежуточная сумма = ", summa)
print("Результат:  ", summa)


# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# Вариант 1. Как у преподавателя
def int_func(world):
    #return world.capitalize() # Так у преподавателя
    return world.title() # поставил так - итог получился - когда отдаём в цикл, то по барабану

input_str = input(" Вводим слова .....")
result_str = []
input_worlds = input_str.split()
for el in input_worlds:
    result_str.append(int_func(el))
print("  ".join(result_str))

# Вариант 2. Как у преподавателя
int_func = lambda word: word.title()
#int_func = lambda word: word.capitalize()
input_str = input(" Вводим слова .....")
result_str = []
input_worlds = input_str.split()
for el in input_worlds:
    result_str.append(int_func(el))
print("  ".join(result_str))



# Вариант 3. Попробовал по своему:

input_str = input(" Вводим слова .....") # вот вот сколько нужно столько и можно
print(input_str.capitalize()) # Вот вот сколько нужно  столько и можно
print(input_str.title()) # Вот Вот Сколько Нужно Столько И Можно

# чисто попробовал: не хочет работать должным образом
# input("Вводим слова .....".capitalize())
# input("Вводим слова .....".title())






