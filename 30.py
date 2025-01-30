# exp2
def calculator():
    while True:
        try:
            operation = input("Введіть операцію (+, -, *, /, ^) або 'вийти' для виходу: ")
            if operation.lower() == 'вийти':
                break

            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))

            if operation == '+':
                print(a + b)
            elif operation == '-':
                print(a - b)
            elif operation == '*':
                print(a * b)
            elif operation == '/':
                if b == 0:
                    raise ZeroDivisionError("Ділення на нуль!")
                print(a / b)
            elif operation == '^':
                if a == 0 and b < 0:
                    raise ValueError("Неможливо звести нуль у негативний ступінь!")
                print(a * b)
            else:
                print("Невірна операція!")

        except (ValueError, ZeroDivisionError) as e:
            print(f"Помилка: {e}")


calculator()

# exp 3

class Employee:
    def __init__(self, first_name, last_name, department, start_year):
        if not first_name or not last_name or not department or start_year < 0:
            raise ValueError("Неправильні дані співробітника.")
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.start_year = start_year

employees = []
while True:
    try:
        first_name = input("Ім'я: ")
        last_name = input("Прізвище: ")
        department = input("Відділ: ")
        start_year = int(input("Рік початку роботи: "))
        employees.append(Employee(first_name, last_name, department, start_year))
    except ValueError as e:
        print(f"Помилка: {e}")

year = int(input("Введіть рік для фільтрації: "))
for emp in employees:
    if emp.start_year > year:
        print(f"{emp.first_name} {emp.last_name}, Відділ: {emp.department}, Рік: {emp.start_year}")

# exp 4
class CustomException(Exception):
    pass

def check_value(value):
    if value < 0:
        raise CustomException("Значення не може бути від'ємним!")

try:
    val = int(input("Введіть невід'ємне число: "))
    check_value(val)
except CustomException as e:
    print(f"Помилка: {e}")

# exp 5
class TrainerNotFound(Exception):
    pass

def sports_complex():
    sports = {"Футбол": "Командна гра", "Теніс": "Індивідуальна гра"}
    trainers = {"Іванов": "Футбол", "Петров": "Теніс"}
    schedules = {"Футбол": "10:00", "Теніс": "11:00"}
    costs = {"Футбол": 20, "Теніс": 15}

    while True:
        print("1 - Види спорту\n2 - Команда тренерів\n3 - Розклад тренувань\n4 - Вартість тренування")
        choice = input("Виберіть пункт або 'вийти': ")

        if choice == '1':
            print(sports)
        elif choice == '2':
            name = input("Введіть прізвище тренера: ")
            try:
                if name not in trainers:
                    raise TrainerNotFound("Тренера не знайдено!")
                print(f"Тренер: {name}, Вид спорту: {trainers[name]}")
            except TrainerNotFound as e:
                print(e)
        elif choice == '3':
            print(schedules)
        elif choice == '4':
            print(costs)
        elif choice.lower() == 'вийти':
            break
        else:
            print("Невірний вибір!")

sports_complex()
