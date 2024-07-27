import socket as soc
import threading as thread

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
port = 5555

def handle_client(c):
    receive = c.recv(1024).decode('utf-8')
    print("\nUser_2: ", receive)

    message = input("You: ")
    c.send(message.encode('utf-8'))

def start_server():
    s.bind(('', port))
    print("Socket is binded to port", port)

    s.listen(5)
    print("Waiting for connection...")

    c, addr = s.accept()
    print("Received connection from ", addr[0])
    
    while True:
        client = thread.Thread(target=handle_client(c))
        client.start()

if __name__ == "__main__":
    start_server()
