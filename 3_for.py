"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
list1 = [{'school_class_4a': '4a', 'scores': [3, 4, 4, 5, 2]}, {'school_class_5a': '4b', 'scores': [4, 5, 5, 3, 4]}]
def main():
    average_score = []  # Средний баллы: 4а, 4б.
    for i in list1:
        score = i['scores']
        result = average_score.append((sum(score)) / len(score))
    print('Средний балл 4 а класса: ', average_score[0])
    print('Средний балл 4 b класса: ', average_score[1])
    print('Средний балл школы: ', sum(average_score) / len(average_score))
if __name__ == "__main__":
    main()
