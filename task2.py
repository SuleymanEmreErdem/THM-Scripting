import socket
import time

ip, port = '10.10.69.122', 1337
num = 0.0

while port != 9765:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print('Connection')
        gRequest = f"GET / HTTP/1.0\r\nHost: {ip}:{port}\r\n\r\n"
        s.send(gRequest.encode('utf8'))
        response = (s.recv(1024).decode('utf-8').split('\r\n\r\n'))[1]
        print('Response:', response)
        
        response = response.split(' ')
        if response[0] == 'add':
            num += float(response[1])
        if response[0] == 'minus':
            num -= float(response[1])
        if response[0] == 'multiply':
            num *= float(response[1])
        if response[0] == 'divide':
            num /= float(response[1])
        port = int(response[2])
        print('Port:', port)
        print('Num:', num)
        print('Sleep 4')
        time.sleep(4)
    except:
        print('!')
