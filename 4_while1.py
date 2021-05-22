"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user(vopros):
  while vopros != otvet:
    vopros = input('Как дела? ')
vopros = input('Как дела? ')
otvet = 'Хорошо'  
if __name__ == "__main__":
    hello_user(vopros)
