#exp2
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))

while True:
    message, address = server.recvfrom(1024)
    device_id = message.decode()
    print(f"Новий пристрій підключено: {device_id} з адреси {address}")

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
device_id = "Device-123"
client.sendto(device_id.encode(), ('localhost', 12345))

#exp3
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12346))

while True:
    message, address = server.recvfrom(1024)
    numbers = list(map(int, message.decode().split(',')))
    total = sum(numbers)
    server.sendto(str(total).encode(), address)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'5,10', ('localhost', 12346))
response, _ = client.recvfrom(1024)
print(f"Сума: {response.decode()}")

#exp 6
import requests
import urllib.request

response = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts')
data = response.read()
print(data)


response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.json())

#exp 7
import socket
import threading
import requests

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Повідомлення: {message}")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12347))
server.listen(5)

while True:
    client_sock, addr = server.accept()
    print(f"Підключено: {addr}")
    threading.Thread(target=handle_client, args=(client_sock,)).start()

#exp8
import requests

def http_client(url, method, data=None):
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=data)
    print(response.status_code, response.headers, response.text)

http_client('https://jsonplaceholder.typicode.com/posts', 'GET')
http_client('https://jsonplaceholder.typicode.com/posts', 'POST', {'title': 'foo', 'body': 'bar', 'userId': 1})
def http_client(url, method, data=None):
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=data)
    print(response.status_code, response.headers, response.text)

http_client('https://jsonplaceholder.typicode.com/posts', 'GET')
http_client('https://jsonplaceholder.typicode.com/posts', 'POST', {'title': 'foo', 'body': 'bar', 'userId': 1})

