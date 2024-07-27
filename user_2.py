import socket as soc

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
port = 5555

def client_communicate():
    s.connect(('127.0.0.1', port))

    while True:
        message = input("\nYou: ")
        s.send(message.encode('utf-8'))

        receive = s.recv(1024)
        print("User_1: ", receive.decode('utf-8'))

if __name__ == "__main__":
    client_communicate() 