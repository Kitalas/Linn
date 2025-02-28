# # exp1
# CREATE TABLE expenses (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     purpose TEXT NOT NULL,
#     amount REAL NOT NULL,
#     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
# );
# # exp2
# import sqlite3
# from datetime import datetime
#
# conn = sqlite3.connect('expenses.db')
# cursor = conn.cursor()
#
# def add_expense():
#     purpose = input("Введіть призначення витрат: ")
#     amount = float(input("Введіть суму витрат: "))
#
#     cursor.execute("INSERT INTO expenses (purpose, amount) VALUES (?, ?)", (purpose, amount))
#     conn.commit()
#     print("Запис успішно додано.")
#
# while True:
#     print("\n--- Особисті витрати ---")
#     print("1. Додати витрати")
#     print("2. Вийти")
#
#     choice = input("Ваш вибір: ")
#     if choice == '1':
#         add_expense()
#     elif choice == '2':
#         break
#     else:
#         print("Невірний вибір, спробуйте ще раз.")
#
# conn.close()
#
# # exp3
# CREATE TABLE financials (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     type TEXT CHECK(type IN ('expense', 'income')) NOT NULL,
#     purpose TEXT NOT NULL,
#     amount REAL NOT NULL,
#     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
# );
#
# # exp4
# def monthly_summary(month, year):
#     cursor.execute("""
#         SELECT type, SUM(amount) FROM financials
#         WHERE strftime('%m', timestamp) = ? AND strftime('%Y', timestamp) = ?
#         GROUP BY type
#     """, (month, year))
#
#     results = cursor.fetchall()
#     for row in results:
#         print(f"{row[0].capitalize()} : {row[1]}")
#
# print("\n--- Огляд фінансів за місяць ---")
# month = input("Введіть місяць (MM): ")
# year = input("Введіть рік (YYYY): ")
# monthly_summary(month, year)
#
# # exp5
# import requests
# import sqlite3
# from datetime import datetime
#
# conn = sqlite3.connect('exchange_rates.db')
# cursor = conn.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS exchange_rates (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     currency_name TEXT NOT NULL,
#     currency_value REAL NOT NULL,
#     current_date DATETIME DEFAULT CURRENT_TIMESTAMP
# )
# """)
#
# def fetch_exchange_rates():
#     response = requests.get("https://api.monobank.ua/bank/currency")
#     return response.json()
#
# def save_exchange_rates(data):
#     for item in data:
#         cursor.execute("""
#             INSERT INTO exchange_rates (currency_name, currency_value, current_date)
#             VALUES (?, ?, ?)
#         """, (item['currencyCodeA'], item['rateSell'], datetime.now()))
#     conn.commit()
#
# exchange_data = fetch_exchange_rates()
# save_exchange_rates(exchange_data)
#
# conn.close()
