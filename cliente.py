#!/usr/bin/env python3

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ip_server = str(input('Digite o ip do servidor: '))
port = 8888

cliente.connect((ip_server, 8888))

terminate = False

print('Digite tt para encerrar o chat')

while True:
    cliente.send(input('Mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'tt':
        break
    else:
        print(msg)
cliente.close()
