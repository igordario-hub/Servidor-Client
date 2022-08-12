from socket import socket, AF_INET, SOCK_DGRAM
HOST = 'localhost'
PORT = 12708

s_client = socket(AF_INET, SOCK_DGRAM)
s_client.connect((HOST, PORT))

cont = int(input('Digite a quantidade de mensagem que você quer enviar:'))

for i in rangue(cont):
    mensage = input('Digite uma mensagem para o servidor\n')
    s_client.sendto(mensage.encode())
    data = s_client.recvfrom(2048)
    reply = data.decode()
    print(f'Servidor:{reply}')

