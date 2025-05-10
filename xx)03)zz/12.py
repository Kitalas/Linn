# exp1
def calculate_speed(distance, time):
    """Обчислити швидкість автомобіля."""
    if time <= 0:
        raise ValueError("Тривалість шляху повинна бути додатнім числом.")
    if distance < 0:
        raise ValueError("Довжина шляху не може бути від'ємною.")
    return distance / time

def test_calculate_speed():
    assert calculate_speed(100, 2) == 50
    assert calculate_speed(0, 5) == 0
    assert calculate_speed(150, 3) == 50
    assert calculate_speed(90, 1.5) == 60
    assert calculate_speed(200, 4) == 50

    try:
        calculate_speed(100, 0)
    except ValueError as e:
        assert str(e) == "Тривалість шляху повинна бути додатнім числом."

    try:
        calculate_speed(-100, 2)
    except ValueError as e:
        assert str(e) == "Довжина шляху не може бути від'ємною."

test_calculate_speed()
print("Всі тести для calculate_speed пройдені.")

# exp2

def calculate_bmi(weight, height):
    """Обчислити індекс маси тіла (BMI)."""
    if height <= 0:
        raise ValueError("Ріст повинен бути додатнім числом.")
    if weight < 0:
        raise ValueError("Вага не може бути від'ємною.")
    return weight / (height * 2)

def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.86  # BMI для 70 кг і 1.75 м
    assert calculate_bmi(0, 1.75) == 0  # BMI для 0 кг
    assert calculate_bmi(60, 1.6) == 23.44  # BMI для 60 кг і 1.6 м

    try:
        calculate_bmi(70, 0)
    except ValueError as e:
        assert str(e) == "Ріст повинен бути додатнім числом."

    try:
        calculate_bmi(-70, 1.75)
    except ValueError as e:
        assert str(e) == "Вага не може бути від'ємною."

test_calculate_bmi()
print("Всі тести для calculate_bmi пройдені.")
# exp3

class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

        if age < 0:
            raise ValueError("Вік не може бути від'ємним числом.")
        if average_grade < 0 or average_grade > 100:
            raise ValueError("Середній бал повинен бути в межах від 0 до 100.")


import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student("Іван", "Іванов", 20, 75),
            Student("Петро", "Петров", 22, 80),
            Student("Оля", "Олененко", 21, 90),
            Student("Саша", "Сидоров", 19, 85),
            Student("Маша", "Майорова", 20, 88),
            Student("Аня", "Антонова", 23, 95),
            Student("Надя", "Надєжда", 22, 70),
            Student("Коля", "Коваленко", 19, 60),
            Student("Лена", "Ленська", 21, 78),
            Student("Женя", "Женін", 20, 92)
        ]

    def test_student_valid_data(self):
        for student in self.students:
            self.assertIsInstance(student.first_name, str)
            self.assertIsInstance(student.last_name, str)
            self.assertIsInstance(student.age, int)
            self.assertIsInstance(student.average_grade, (int, float))
            self.assertGreaterEqual(student.age, 0)
            self.assertGreaterEqual(student.average_grade, 0)
            self.assertLessEqual(student.average_grade, 100)

    def test_student_invalid_age(self):
        with self.assertRaises(ValueError):
            Student("Аня", "Антонова", -1, 70)


def test_student_invalid_average_grade(self):
    with self.assertRaises(ValueError):
        Student("Ігор", "Ігоренко", 30, 150)  # Неправильний середній бал


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
