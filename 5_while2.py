"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'Привет': 'Здорова', 'Как дела?': 'Хорошо', 'Что делаешь?':'Программирую'}

def ask_user(answers_dict):
  if answers_dict in questions_and_answers:
    print(questions_and_answers[answers_dict])
  else:
    answers_dict = input('Задайте вопрос ')
answers_dict = input('Задайте вопрос ')
if __name__ == "__main__":
    ask_user(answers_dict)