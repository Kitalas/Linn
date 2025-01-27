# exp1
class Editor:
    def view_document(self):
        print("Перегляд документа.")

    def edit_document(self):
        print("Редагування документів недоступне для безкоштовної версії.")

class ProEditor(Editor):
    def edit_document(self):
        print("Редагування документа доступне.")

key = input("Введіть ліцензійний ключ: ")
if key == "правильний_ключ":
    editor = ProEditor()
else:
    editor = Editor()

editor.view_document()
editor.edit_document()

# exp2
class GraphicObject:
    def draw(self):
        print("Малювання графічного об'єкта.")

class Rectangle(GraphicObject):
    def draw(self):
        print("Малювання прямокутника.")

class ClickableObject:
    def click(self):
        print("Об'єкт натиснуто.")

class Button(ClickableObject):
    def click(self):
        print("Кнопка натиснута.")


button = Button()
rectangle = Rectangle()

button.click()
rectangle.draw()

#exp3

class A:
    def method(self):
        print("Метод класу A.")

class B(A):
    def method(self):
        print("Метод класу B.")
        super().method()

class C(A):
    def method(self):
        print("Метод класу C.")
        super().method()

class D(B, C):
    def method(self):
        print("Метод класу D.")
        super().method()

d = D()
d.method()

# exp5
def adult_check(func):
    def wrapper(*args, *kwargs):
        age = func(*args, *kwargs)
        return age >= 18

    return wrapper

@adult_check
def age_in_ukraine(years):
    return years

@adult_check
def age_in_usa(years):
    return years

# exp6
def count_adults(func):
    def wrapper(cls):
        objects = func(cls)
        adults = [obj for obj in objects if obj.age >= 18]
        return len(adults)

    return wrapper

class Person:
    def __init__(self, age):
        self.age = age

@count_adults
def get_people(cls):
    return [cls(20), cls(16), cls(30)]

# exp7
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}")

class Car(Vehicle):
    def info(self):
        print(f"Автомобіль - Марка: {self.brand}, Модель: {self.model}")

class Bicycle(Vehicle):
    def info(self):
        print(f"Велосипед - Марка: {self.brand}, Модель: {self.model}")

car = Car("Toyota", "Camry")
bicycle = Bicycle("Giant", "Escape 3")

car.info()
bicycle.info()