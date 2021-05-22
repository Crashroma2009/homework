"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
spisok = [{'school_class_4a': '4a', 'scores': [3, 4, 4, 5, 2]}, {'school_class_5a': '4b', 'scores_1': [4, 5, 5, 3, 4]}]
def main():
    ratings = 0
    n = 0
    for i in spisok[0]['scores']:
        ratings += i
        n += 1
    sr_ball_4a = ratings / len(spisok[0]['scores'])
    print('Средний балл 4 а класса: ', sr_ball_4a)

    ratings1 = 0
    n1 = 0
    for k in spisok[1]['scores_1']:
        ratings1 += k
        n1 += 1
    sr_ball_4b = ratings1 / len(spisok[1]['scores_1'])
    print('Средний балл 4 b класса: ', sr_ball_4b)

    summ = (ratings + ratings1) / (n + n1)
    print('Средний балл школы: ', summ)
if __name__ == "__main__":
    main()
