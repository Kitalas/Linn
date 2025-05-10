# exp1
from typing import List


def int_to_str_list(int_list: List[int]) -> List[str]:
    return [str(i) for i in int_list]



print(int_to_str_list([1, 2, 3, 4]))

# exp2
from typing import List, Optional


class File:
    def __init__(self, name: str, directory: Optional['Directory'] = None):
        self.name: str = name
        self.directory: Optional[Directory] = directory


class Directory:
    def __init__(self, name: str, root: Optional['Directory'] = None):
        self.name: str = name
        self.root: Optional[Directory] = root
        self.files: List[File] = []
        self.sub_directories: List['Directory'] = []

    def add_sub_directory(self, sub_directory: 'Directory') -> None:
        sub_directory.root = self
        self.sub_directories.append(sub_directory)

    def remove_sub_directory(self, sub_directory: 'Directory') -> None:
        sub_directory.root = None
        self.sub_directories.remove(sub_directory)

    def add_file(self, file: File) -> None:
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File) -> None:
        file.directory = None
        self.files.remove(file)

root_dir = Directory("Root")
sub_dir = Directory("Sub")
root_dir.add_sub_directory(sub_dir)
file1 = File("file1.txt")
root_dir.add_file(file1)

# exp3
import sqlite3
import smtplib
import datetime
from typing import List, Optional


class User:
    def __init__(self, first_name: str, last_name: str, middle_name: str, birthday: datetime.date):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.middle_name: str = middle_name
        self.birthday: datetime.date = birthday
        self.email: Optional[str] = None

    def get_full_name(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self) -> str:
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_age(self) -> int:
        today = datetime.date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    def __str__(self) -> str:
        return f"{self.get_full_name()}, {self.birthday}"


def register_user(user: User):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (first_name TEXT, last_name TEXT, middle_name TEXT, birthday TEXT, email TEXT)''')
    cursor.execute("INSERT INTO users (first_name, last_name, middle_name, birthday, email) VALUES (?, ?, ?, ?, ?)",
                   (user.first_name, user.last_name, user.middle_name, user.birthday.isoformat(), user.email))
    conn.commit()
    conn.close()

    send_email(user)


def send_email(user: User):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"
    password = "your_password"

    message = f"Subject: Дякуємо за реєстрацію\n\nШановний(а) {user.get_full_name()}, дякуємо за реєстрацію!"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, user.email, message)


def find_users(first_name: str, last_name: str, email: str) -> List[User]:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT first_name, last_name, middle_name, birthday, email FROM users WHERE first_name=? OR last_name=? OR email=?",

    (first_name, last_name, email))
    results = cursor.fetchall()
    conn.close()

    return [User(first_name=row[0], last_name=row[1], middle_name=row[2], birthday=datetime.date.fromisoformat(row[3]))
            for row in results]

new_user = User("Ігор", "Петров", "Сергійович", datetime.date(1990, 1, 1))
new_user.email = "user_email@example.com"
register_user(new_user)

found_users = find_users("Ігор", "", "")
for user in found_users:
    print(user)