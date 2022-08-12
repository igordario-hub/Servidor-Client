from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread



def HandleRequest(conn_socket, addr_client):
    while True:
        print('Próxima mensagem')
        data = s_client.recvfrom(2048)
        print(f'Cliente {addr_client}')
        requi = data.decode()
        requi= 'ok'
        s_client.sendto(rep.encode())

HOST = 'localhost'
PORT = 12708

#criando Socket
s_servidor = socket(AF_INET, SOCK_DGRAM)
print('Socket criado com sucesso!')
s_servidor.bind((HOST, PORT))
s_servidor.listen()

while True:
    conn_socket, addr_client
    print(f'O servidor aceitou a conexão do Cliente: {addr_client}')
    Thread(target=HandleRequest, args=(conn_socket, addr_client)).start()



