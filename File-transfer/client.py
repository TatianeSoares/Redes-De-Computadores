import socket
from time import sleep, time
import os

HOST = input("Insira o ip no qual deseja se conectar: ")
PORT = input("Insira a porta: ")
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SEPARATOR = "<SEPARATOR>"
bufferSize = int(input("Insira o tamanho do buffer: "))


def sendFile(file, ):
    i = 0
    size = os.path.getsize(file)
    print("Tamanho do arquivo a ser enviado: ", size)
    tcp.send(f"{str(bufferSize)}{SEPARATOR}{file}{SEPARATOR}{size}".encode('utf-8'))
    sleep(5)
    with open(file, 'rb') as arq:
        inicio = time()
        while True:
            bytesToSend = arq.read(bufferSize)
            if not bytesToSend:
                fim = time()
                break
            tcp.sendall(bytesToSend)
            i += 1

    print("Tempo de transmissão: ", (fim - inicio))
    print("Total de pacotes enviados: ", i)

    tcp.close()
    return


def main():
    global HOST
    global PORT

    try: 
        dest = (HOST, int(PORT))
        tcp.connect(dest)
    except Exception as e:
        print(e)
        return

    # threading.Thread(target=recvMsg).start()
    file = input("Insira o arquivo: ")
    sendFile(file)

    # while True:
    #     msg = input()
    #     tcp.send(bytes(msg, "utf8"))
    #     sleep(0.1)




main()