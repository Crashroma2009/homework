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
    if isinstance(str1, int) and isinstance(str2, int):
        return '0'
    elif str1 == str2:
         return '1'
    elif str1 != str2 and len(str1) > len(str2):
         return '2'
    elif str1 != str2 and str2 == 'learn':
        return '3'
    
if __name__ == "__main__":
    # 1 раз
  print(main('Python', 'learn'))  
  # 2 раз
  print(main('Moscow', 'Moscow'))  
  # 3 раз
  print(main('prog', 'learn')) 
  # 4 раз
  print(main(3, 54))
