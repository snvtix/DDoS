import socket
import threading
from datetime import datetime

def aktualna_godzina():
    teraz = datetime.now()

    godzina = teraz.hour
    minuta = teraz.minute
    sekunda = teraz.second

    return f"{godzina:02d}:{minuta:02d}:{sekunda:02d}"

def handle_client(client_socket, addr):
    print(f"Nawiązano połączenie z klientem TCP o adresie {addr}.")

    while True:
        data = client_socket.recv(1024)
        if data == b"Jaka jest teraz godzina?":
            print("Klient pyta sie o godzinę, muszę odpowiedzieć.")
            str = aktualna_godzina()
            bytes_data = str.encode('utf-8')
            client_socket.sendall(bytes_data)
        else:
            print("Klient chce ode mnie usługi której nie oferuję.")
            break
        data = client_socket.recv(1024)
        if data == b"Dzieki!":
            print("Klient mi podziękował, to miłe :3")
            client_socket.sendall(b"Nie ma sprawy :)")
            break
        else:
            print("Klient mnie nie docenia :(")
            break

    print(f"Połączenie z klientem TCP o adresie {addr} zakończyło się.")
    client_socket.close()

def start_server():
    server_ip = '192.168.1.12'
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Nasłuchuję na {server_ip} : {server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()