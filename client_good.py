import socket

def start_client():
    server_ip = '192.168.1.12'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while(True):
        client_socket.sendall(b"Jaka jest teraz godzina?")
        data = client_socket.recv(1024)
        if data:
            print(f"Aktualna godzina to: {data}")
            client_socket.sendall(b"Dzięki!")
            data = client_socket.recv(1024)
            if data == b"Nie ma sprawy :)":
                print("Ten serwer jest pomocny...")
                break
            else:
                print("ERROR")
                break
        else:
            print("ERROR")
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()