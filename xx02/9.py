# exp1
import random

with open('random_numbers.txt', 'w') as file:
    for _ in range(10000):
        file.write(f"{random.uniform(0, 100)}\n")

with open('random_numbers.txt', 'r') as file:
    total_sum = sum(float(line) for line in file)
print(f"Сума чисел: {total_sum}")

# # exp 2
# import shelve
#
# def shorten_url(url):
#     with shelve.open('url_database') as db:
#         short_url = generate_short_url(url)
#         db[short_url] = url
#         return short_url
#
# def get_url(short_url):
#     with shelve.open('url_database') as db:
#         return db.get(short_url)

# exp3

import pickle
import json

products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 499.99},
    {"name": "Headphones", "price": 199.99}
]

# Серіалізація з pickle
with open('products.pkl', 'wb') as pkl_file:
    pickle.dump(products, pkl_file)

# Збереження у JSON
with open('products.json', 'w') as json_file:
    json.dump(products, json_file)