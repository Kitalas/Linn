# exp2
class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"{self.surname} {self.name}, {self.age}, {self.mob_phone}, {self.email}"

    def sent_message(self, message):
        return f"Sent to {self.mob_phone}: {message}"


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"{self.name} works as {self.job}"


contact1 = Contact("Doe", "John", 30, "123-456-7890", "john@example.com")
update_contact1 = UpdateContact("Smith", "Jane", 25, "098-765-4321", "jane@example.com", "Engineer")

print(dict(contact1.__dict__))
print(Contact.__bases__)
print(UpdateContact.__bases__)

# exp3
for attr in ['surname', 'name', 'age', 'mob_phone', 'email']:
    print(hasattr(contact1, attr), getattr(contact1, attr), end=', ')
    setattr(contact1, attr, "Updated")
    print(getattr(contact1, attr), end=', ')
    delattr(contact1, attr)
    print(hasattr(contact1, attr))

# exp4
contact2 = Contact("Brown", "Emily", 28, "123-123-1234", "emily@example.com")
update_contact2 = UpdateContact("Green", "Luke", 35, "321-321-4321", "luke@example.com", "Manager")

print(isinstance(contact1, Contact))  # True
print(isinstance(update_contact1, UpdateContact))  # True
print(issubclass(UpdateContact, Contact))  # True

# exp5
print(contact1.__dict__)
print(update_contact1.__dict__)

del update_contact1.job
print(update_contact1.__dict__)

# exp6
print(dir(Contact))
print(dir(UpdateContact))
