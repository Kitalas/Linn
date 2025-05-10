# exp1
def iterate_iterable(iterable):
    for item in iterable:
        print(item)

my_list = [1, 2, 3, 4, 5]
iterate_iterable(my_list)

# exp2
class MyList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def clear(self):
        self.items.clear()

    def add_at(self, index, item):
        self.items.insert(index, item)

    def remove(self):
        if self.items:
            self.items.pop()

    def remove_at(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]

    def __str__(self):
        return str(self.items)

my_list = MyList()
my_list.add(1)
my_list.add(2)
my_list.add_at(1, 3)
print(my_list)  # [1, 3, 2]
my_list.remove()
print(my_list)  # [1, 3]
my_list.remove_at(0)
print(my_list)  # [3]
my_list.clear()
print(my_list)  # []

# exp 3
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

my_list = [1, 2, 3, 4, 5]
for item in ReverseIterator(my_list):
    print(item)
