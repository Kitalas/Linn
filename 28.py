# exp1
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

# exp 2
class English:
    def greeting(self):
        return "Hello, friend!"

class Spanish:
    def greeting(self):
        return "¡Hola, amigo!"

def hello_friend():
    eng = English()
    esp = Spanish()
    print(eng.greeting())
    print(esp.greeting())

hello_friend()

# exp3
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9


# exp5
import matplotlib.pyplot as plt
import numpy as np

class Shape:
    def area(self):
        pass

class Cone(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return np.pi * self.radius * (self.radius + np.sqrt(self.height*2 + self.radius*2))

class Paraboloid(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return np.double(np.pi * self.a * self.b)

cone = Cone(3, 4)
paraboloid = Paraboloid(2, 3)

print("Cone area:", cone.area())
print("Paraboloid area:", paraboloid.area())

# Visualization example (paraboloid)
X = np.linspace(-3, 3, 100)
Y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(X, Y)
Z = (X*2) / 4 + (Y*2) / 9  # Example equation for a paraboloid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5)
plt.show()
