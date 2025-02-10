# exp1
import random

with open('random_numbers.txt', 'w') as file:
    for _ in range(10000):
        file.write(f"{random.uniform(0, 100)}\n")

with open('random_numbers.txt', 'r') as file:
    total_sum = sum(float(line) for line in file)

print(f"Сума чисел: {total_sum}")


# # exp 2
import shelve
import random
import string

def generate_short_url(length=6):
    """Генерує короткий URL з випадкових букв і цифр."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def shorten_url(url):
    """Скорочує URL і зберігає його в базі даних."""
    with shelve.open('url_database') as db:
        short_url = generate_short_url()
        while short_url in db:
            short_url = generate_short_url()
        db[short_url] = url
        return short_url

def get_url(short_url):
    """Отримує оригінальний URL за коротким."""
    with shelve.open('url_database') as db:
        return db.get(short_url, "URL не знайдено.")

if __name__ == "__main__":
    url_to_shorten = input("Введіть URL для скорочення: ")
    short_url = shorten_url(url_to_shorten)
    print(f"Скорочений URL: {short_url}")

    retrieved_url = get_url(short_url)
    print(f"Оригінальний URL: {retrieved_url}")

# exp3
import pickle
import json

products = [
    {"name": "Laptop", "price": 999.99, "category": "Electronics"},
    {"name": "Smartphone", "price": 499.99, "category": "Electronics"},
    {"name": "Headphones", "price": 199.99, "category": "Accessories"},
    {"name": "Coffee Maker", "price": 79.99, "category": "Home Appliances"},
    {"name": "Book", "price": 15.99, "category": "Books"}
]

with open('products.pkl', 'wb') as pkl_file:
    pickle.dump(products, pkl_file)

with open('products.json', 'w') as json_file:
    json.dump(products, json_file)

print("Список товарів успішно збережено у форматах pickle та JSON.")
