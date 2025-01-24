# exp1
class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year} (Genre: {self.genre})"

# Створення кількох книжок
book1 = Book("George Orwell", "1984", 1949, "Dystopian")
book2 = Book("J.K. Rowling", "Harry Potter and the Philosopher's Stone", 1997, "Fantasy")
book3 = Book("F. Scott Fitzgerald", "The Great Gatsby", 1925, "Classic")

# Вивід книг
print(book1)
print(repr(book2))
print(book3)

# exp2
class Review:
    def __init__(self, reviewer, content):
        self.reviewer = reviewer
        self.content = content

    def __str__(self):
        return f"{self.reviewer}: {self.content}"

class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def __str__(self):
        reviews_str = "\n".join(str(review) for review in self.reviews) if self.reviews else "No reviews yet."
        return f"'{self.title}' by {self.author}, published in {self.year} (Genre: {self.genre})\nReviews:\n{reviews_str}"

book1 = Book("George Orwell", "1984", 1949, "Dystopian")
review1 = Review("Alice", "A thought-provoking novel.")
review2 = Review("Bob", "A chilling depiction of a totalitarian regime.")
book1.add_review(review1)
book1.add_review(review2)

print(book1)

# exp4
class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model}, Price: ${self.price}"

class Showroom:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def sell_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            return f"{car} sold."
        else:
            return "Car not available for sale."

    def list_cars(self):
        if not self.cars:
            return "No cars available for sale."
        return "\n".join(str(car) for car in self.cars)

car1 = Car("Toyota", "Camry", 2020, 24000)
car2 = Car("Honda", "Civic", 2019, 22000)
car3 = Car("Ford", "Mustang", 2021, 35000)

showroom = Showroom()
showroom.add_car(car1)
showroom.add_car(car2)
showroom.add_car(car3)

print("Available cars:")
print(showroom.list_cars())

print(showroom.sell_car(car2))

print("\nAvailable cars after sale:")
print(showroom.list_cars())