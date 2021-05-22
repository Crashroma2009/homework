"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str1, str2):
    if str1 != str(str1) and str2 != str(str2):
         print('0')
    elif str1 == str2:
         print('1')
    elif str1 != str2 and len(str1) > len(str2):
         print('2')
    elif str1 != str2 and str2 == 'learn':
        print('3')
    
if __name__ == "__main__":
    # 1 раз
  str1 = 'Python'
  str2 = 'learn'
  main(str1, str2)
  # 2 раз
  str1 = 'Moscow'
  str2 = 'Moscow'
  main(str1, str2)
  # 3 раз
  str1 = 'prog'
  str2 = 'learn'
  main(str1, str2)
  # 4 раз
  str1 = 3
  str2 = 54
  main(str1, str2)
