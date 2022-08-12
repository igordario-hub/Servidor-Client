from socket import socket, AF_INET, SOCK_STREAM

s_client = socket(AF_INET, SOCK_DGRAM)
s_client.connect((HOST, 12708))

cont = int(input('Digite a quantidade de mensagem que você quer enviar:'))
                 
for i in rangue(cont):
    mensage = input('Digite uma mensagem para o servidor\n')
    s_client.send(mensage.encode())
    data = s_client.recv(2048)
    reply = data.decode()
    print(f'Servidor:{reply}')
