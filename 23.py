#exp1
import json
data = {'name': 'John', 'age': 30, 'city': 'New York'}
jsonstring = json.dumps(data)

with open('data.json', 'w') as f:
    f.write(jsonstring)

with open('data.json', 'r') as f:
    dataloaded = json.load(f)

#exp3
import csv

class CustomDialect(csv.Dialect):
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTEMINIMAL

csv.registerdialect('custom', CustomDialect)
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='custom')
    writer.writerow('name', 'age')
    writer.writerow('John', 30)

with open('data.csv', 'r') as f:
    reader = csv.reader(f, dialect='custom')