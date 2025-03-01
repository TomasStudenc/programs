import threading
import socket
import time
import struct
import os
import time
from random import randint as rd

from PIL.ImageSequence import all_frames
from contourpy.util.data import random
from matplotlib.pyplot import connect

# Flag definitions
SYN = 0x01  # 00000001
ACK = 0x02  # 00000010
TEXT = 0x04  # 00000100
FILE = 0x08  # 00001000
FIN = 0x10  # 00010000
RESEND = 0x20  # 00100000
END = 0x40  # 01000000
HRT = 0x80  # 10000000
fragment_size = 0
save_path = ""
# Header structure: flag (1 byte), checksum (4 bytes), frag_num (1 byte), frag_count (1 byte)
HEADER_FORMAT = '!BIII'  # B = 1 byte, I = 4 bytes, I = 4 byte, I = 4 byte || 13byte
REZIA_HEDER_FORMAT = '!B' #B = 1 byte
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
REZIA_SIZE = struct.calcsize(REZIA_HEDER_FORMAT)
witch_frag = None


def crc32(data):
    if isinstance(data, str):
        data = data.encode('utf-8')

    polynomial = 0xEDB88320
    crc = 0xFFFFFFFF

    for byte in data:
        crc ^= byte

        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1

    return crc ^ 0xFFFFFFFF


class Client:
    def __init__(self, ip, port_receive, client_2_ip, c2_port_receive) -> None:
        self.sock_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_ip = client_2_ip
        self.server_port_receive = c2_port_receive

        self.local_port_sum = port_receive
        self.remote_port_sum = c2_port_receive
        self.sock_receive.bind((ip, port_receive))
        self.sock_receive.settimeout(5)
        self.heartbeat_interval = 5
        self.running = True
        self.client = None
        self.heartbeat_missed_count = 0
        self.max_missed_heartbeats = 3  # Max number of missed heartbeats before quitting

        # Shared state for acknowledgment
        self.acknowledged_event = threading.Event()
        self.acknowledged_event_HRT = threading.Event()
        self.resend_event = threading.Event()
        # missing fragmet variable
        self.witch_frag = None

    def listen_for_handshake(self):
        connected = False
        while not connected and self.running:
            try:
                print("Listening for handshake...")
                data, self.client = self.sock_receive.recvfrom(1024)
                # Unpack the header
                flag = struct.unpack(REZIA_HEDER_FORMAT, data[:REZIA_SIZE])[0]
                if flag == SYN:
                    #print(f"Received SYN from {self.server_ip}")
                    # Send SYN-ACK with new header
                    response_header = struct.pack(REZIA_HEDER_FORMAT, SYN | ACK)
                    self.sock_send.sendto(response_header, (self.server_ip, self.server_port_receive))
                    #print(f"Sent SYN-ACK to {self.server_ip}")
                    # Wait for ACK
                    data, _ = self.sock_receive.recvfrom(1024)
                    flag = struct.unpack(REZIA_HEDER_FORMAT, data[:REZIA_SIZE])[0]
                    if flag == ACK:
                        #print("Received ACK")
                        print("Handshake complete. Connection established.")
                        # threading.Thread(target=self.receive_message).start()
                        connected = True
                        # threading.Thread(target=self.monitor_connection).start()
            except socket.timeout:
                print("Timeout while listening for handshake, retrying...")

    def initiate_handshake(self):
        connected = False
        while not connected and self.running:
            try:
                print("Attempting handshake...")
                # Send SYN with new header
                self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT,SYN), (self.server_ip, self.server_port_receive))
                #print("Sent SYN")
                # Wait for SYN-ACK
                data, _ = self.sock_receive.recvfrom(1024)
                flag = struct.unpack(REZIA_HEDER_FORMAT, data[:REZIA_SIZE])[0]
                if flag == (SYN | ACK):
                    #print("Received SYN-ACK")
                    # Send final ACK
                    #print("Sent ACK")
                    self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, ACK),
                                          (self.server_ip, self.server_port_receive))
                    print("Handshake complete. Connection established.")
                    # threading.Thread(target=self.monitor_connection).start()
                    connected = True
            except socket.timeout:
                print("No response, retrying handshake...")

        return connected

    def send_message(self):
        global fragment_size, last_frag_size
        frag = {}
        while self.running:
            command = input("Pre posielanie textu zadaj 'T'\nPre posielanie súborov zadaj 'F'\nak chces ukončit spojenie zadaj 'KILL':\n").strip().upper()
            if command == "KILL":
                try:
                    # Send FIN with new header
                    self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, FIN),
                                          (self.server_ip, self.server_port_receive))
                except socket.error as e:
                    print(end="")
                self.quit()
                break
            elif command == "T":
                fragment_size = int(input("Enter fragment size:\n"))
                while fragment_size>1459:
                    print("fragment size too long, try again")
                    fragment_size = int(input("Enter fragment size:\n"))
                corupt = input("Ak chces corruptnut spravu zadaj \"y\":\n").strip().upper()
                message = input("Zadaj správu: ")
                message_coded = message.encode()
                fragment_count = (len(message_coded) + fragment_size - 1) // fragment_size

                for frag_num in range(fragment_count):
                    if not self.running:
                        break
                    start_index = frag_num * fragment_size
                    end_index = start_index + fragment_size
                    fragment = message_coded[start_index:end_index]

                    checksum = crc32(fragment)
                    flag = TEXT

                    header = struct.pack(HEADER_FORMAT, flag, checksum, frag_num, fragment_count)
                    data_to_send = header + fragment
                    frag[frag_num] = data_to_send
                    if corupt == "Y":
                        if rd(0, 1) == 1:
                            checksum += 1
                    try:
                        self.sock_send.sendto(
                            struct.pack(HEADER_FORMAT, flag, checksum, frag_num, fragment_count) + fragment,
                            (self.server_ip, self.server_port_receive))
                    except socket.error:
                        continue
                try:
                    self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, TEXT | END),
                                          (self.server_ip, self.server_port_receive))
                except socket.error:
                    print(end="")
                if self.running:
                    print("--------------------------------------------------")
                    print(f"size of the message {len(message_coded)}")
                    print(f"numebr of fragments {fragment_count}")
                    all_frag = len(frag[0][HEADER_SIZE:])
                    last_frag = len(frag[fragment_count - 1][HEADER_SIZE:])
                    if all_frag == last_frag:
                        print(f"all fragments size {all_frag}")
                    else:
                        print(f"fragment size {all_frag}")
                        print(f"last fragment size {last_frag}")
                    print("--------------------------------------------------")
                self.acknowledged_event.clear()
                self.resend_event.clear()
                while self.running:
                    if self.acknowledged_event.is_set():
                        print("message recived succesfuly")
                        break
                    if self.resend_event.is_set():
                        if self.witch_frag == -1:
                            self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, TEXT | END),
                                                  (self.server_ip, self.server_port_receive))
                        else:
                            data_to_send = frag[self.witch_frag]
                            self.sock_send.sendto(data_to_send, (self.server_ip, self.server_port_receive))
                            self.resend_event.clear()
                            self.witch_frag = None
                            self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, TEXT | END),
                                                  (self.server_ip, self.server_port_receive))
                frag = {}




            elif command == "F":
                fragment_size = int(input("Enter fragment size:\n"))
                while fragment_size > 1459:
                    print("fragment size too long, try again")
                    fragment_size = int(input("Enter fragment size:\n"))
                corupt = input("Ak chces corruptnut spravu zadaj 'y':\n").strip().upper()

                path_to_file = input("Zadaj cestu k súboru: ")
                if not os.path.exists(path_to_file):
                    print("path not found")
                    continue
                file_name = os.path.basename(path_to_file).encode()
                header = struct.pack(HEADER_FORMAT, FILE, 0, 0, 0)
                self.sock_send.sendto(header + file_name, (self.server_ip, self.server_port_receive))

                with open(path_to_file, 'rb') as f:
                    fragment_count = (os.path.getsize(path_to_file) + fragment_size - 1) // fragment_size

                    for frag_num in range(fragment_count):
                        if not self.running:
                            break
                        fragment = f.read(fragment_size)
                        checksum = crc32(fragment)
                        header = struct.pack(HEADER_FORMAT, FILE, checksum, frag_num, fragment_count)
                        data_to_send = header + fragment
                        frag[frag_num] = data_to_send
                        if corupt == "Y":
                            if frag_num == 5 or frag_num == 150:
                                checksum += 1
                            # if rd(0, 1) == 1:
                            #     checksum += 1
                        try:
                            self.sock_send.sendto(
                                struct.pack(HEADER_FORMAT, FILE, checksum, frag_num, fragment_count) + fragment,
                                (self.server_ip, self.server_port_receive))
                        except socket.error:
                            time.sleep(5)
                            continue
                try:
                    self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, FILE | END),
                                          (self.server_ip, self.server_port_receive))
                except socket.error:
                    print(end="")
                if self.running:
                    print("--------------------------------------------------")
                    print(f"name of file {file_name}")
                    print(f"path to file {path_to_file}")
                    print(f"size of file {(os.path.getsize(path_to_file) / 1024):.3f} KB")
                    print(f"number of fragments {fragment_count}")
                    all_frag = len(frag[0][HEADER_SIZE:])
                    last_frag = len(frag[fragment_count - 1][HEADER_SIZE:])
                    if all_frag == last_frag:
                        print(f"all fragments size {all_frag}")
                    else:
                        print(f"fragment size {all_frag}")
                        print(f"last fragment size {last_frag}")
                    print("--------------------------------------------------")
                self.acknowledged_event.clear()
                self.resend_event.clear()
                while self.running:
                    if self.acknowledged_event.is_set():
                        print("file recived succesfuly")
                        break
                    if self.resend_event.is_set():
                        if self.witch_frag == -1:
                            self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, FILE | END),
                                                  (self.server_ip, self.server_port_receive))
                        else:
                            data_to_send = frag[self.witch_frag]
                            self.sock_send.sendto(data_to_send, (self.server_ip, self.server_port_receive))
                            self.resend_event.clear()
                            self.witch_frag = None
                            self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, FILE | END),
                                                  (self.server_ip, self.server_port_receive))
                frag = {}

    def receive_message(self):
        fragments = {}
        file_name = None
        total_fragments = 0
        connection_lost = False

        while self.running:
            try:
                data, self.client = self.sock_receive.recvfrom(1500)
                # Unpack the header
                flag= struct.unpack(REZIA_HEDER_FORMAT, data[:REZIA_SIZE])[0]
                client_ip, _ = self.client

                if flag == HRT:
                    self.heartbeat_missed_count = 0
                    self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, HRT | ACK),
                                          (client_ip, self.server_port_receive))
                    if connection_lost == True:
                        self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, HRT | RESEND),
                                              (client_ip, self.server_port_receive))
                        connection_lost = False
                elif flag == HRT | ACK:
                    self.heartbeat_missed_count = 0
                    self.acknowledged_event_HRT.set()
                elif flag == HRT | RESEND:
                    self.witch_frag = -1
                    self.resend_event.set()
                elif flag == RESEND:
                    _, _, frag_num, _ = struct.unpack(HEADER_FORMAT, data[:HEADER_SIZE])
                    self.witch_frag = frag_num
                    self.resend_event.set()
                elif flag == FIN:
                    print("Termination flag received. Closing connection.")
                    self.quit()
                    break
                elif flag == FILE:
                    _, checksum, frag_num, frag_count = struct.unpack(HEADER_FORMAT, data[:HEADER_SIZE])
                    self.heartbeat_missed_count = 0
                    if file_name is None:
                        start_time = time.time()
                        try:
                            file_name = data[HEADER_SIZE:].decode('utf-8')
                        except UnicodeDecodeError:
                            file_name = "error.by"
                    else:
                        txt_data = data[HEADER_SIZE:]
                        if crc32(txt_data) != checksum:
                            print(f"Received file fragment {frag_num + 1} of {frag_count},state : corupted")
                        else:
                            print(f"Received file fragment {frag_num + 1} of {frag_count},state : good")
                        fragments[frag_num] = data
                        total_fragments = frag_count

                elif flag == FILE | END:
                    all_good = 0
                    for j in range(total_fragments):
                        _, checksum, _, _ = struct.unpack(HEADER_FORMAT, fragments[j][:HEADER_SIZE])
                        if not j in fragments:
                            self.sock_send.sendto(struct.pack(HEADER_FORMAT, RESEND, 0, j, 0),
                                                  (client_ip, self.server_port_receive))
                            break
                        elif crc32(fragments[j][HEADER_SIZE:]) != checksum:
                            del fragments[j]
                            self.sock_send.sendto(struct.pack(HEADER_FORMAT, RESEND, 0, j, 0),
                                                  (client_ip, self.server_port_receive))
                            break
                        else:
                            all_good += 1
                    if all_good == total_fragments:
                        end_time = time.time() - start_time
                        print("--------------------------------------------------")
                        print(f"čas prenosu {end_time:.2f} sec")

                        self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, FILE | ACK),
                                              (client_ip, self.server_port_receive))
                        file_path = save_path + "\\" + file_name
                        with open(file_path, 'wb') as f:
                            for i in range(total_fragments):
                                f.write(fragments[i][HEADER_SIZE:])
                            print(f"File '{file_name}' received successfully.")
                            print(f"path to file: {file_path}")
                        print(f"počet fragmentov= {total_fragments}")
                        print(f"size of file: {(os.path.getsize(file_path)) / 1024:.3f} KB")
                        frag_size = len(fragments[0][HEADER_SIZE:])
                        last_size = len(fragments[total_fragments - 1][HEADER_SIZE:])
                        if last_size == frag_size:
                            print(f"all fragmetns have size of {frag_size}")
                        else:
                            print(f"fragmet size: {frag_size}")
                            print(f"last fragment size: {last_size}")
                        print("--------------------------------------------------")
                        file_name = None
                        total_fragments = 0
                        fragments = {}
                        connection_lost = False

                elif flag == FILE | ACK:
                    self.acknowledged_event.set()

                elif flag == TEXT:
                    _, checksum, frag_num, frag_count = struct.unpack(HEADER_FORMAT, data[:HEADER_SIZE])
                    txt_data = data[HEADER_SIZE:]
                    if frag_num == 0:
                        start_time = time.time()
                    if crc32(txt_data) != checksum:
                        print(f"Received text fragment {frag_num + 1} of {frag_count},state : corupted")
                    else:
                        print(f"Received text fragment {frag_num + 1} of {frag_count},state : good")
                    fragments[frag_num] = data
                    total_fragments = frag_count

                elif flag == TEXT | END:
                    all_good = 0
                    for j in range(total_fragments):
                        _, checksum, _, _ = struct.unpack(HEADER_FORMAT, fragments[j][:HEADER_SIZE])
                        if not j in fragments:
                            self.sock_send.sendto(struct.pack(HEADER_FORMAT, RESEND, 0, j, 0),
                                                  (client_ip, self.server_port_receive))
                            break
                        elif crc32(fragments[j][HEADER_SIZE:]) != checksum:
                            del fragments[j]
                            self.sock_send.sendto(struct.pack(HEADER_FORMAT, RESEND, 0, j, 0),
                                                  (client_ip, self.server_port_receive))
                            break
                        else:
                            all_good += 1
                    if all_good == total_fragments:
                        self.sock_send.sendto(struct.pack(REZIA_HEDER_FORMAT, TEXT | ACK),
                                              (client_ip, self.server_port_receive))
                        full_message = b''.join(fragments[frg][HEADER_SIZE:] for frg in range(total_fragments))
                        print("--------------------------------------------------")
                        print(f"Received message from {client_ip}: {full_message.decode('utf-8')}")
                        print(f"number of fragments {total_fragments}")
                        print(f"size of message {len(full_message)} bytes")
                        frag_size = len(fragments[0][HEADER_SIZE:])
                        last_size = len(fragments[total_fragments - 1][HEADER_SIZE:])
                        end_time = time.time() - start_time
                        print(f"čas prenosu {end_time:.2f} sec")
                        if last_size == frag_size:
                            print(f"all fragmetns have size of {frag_size}")
                        else:
                            print(f"fragmet size: {frag_size}")
                            print(f"last fragment size: {last_size}")
                        print("--------------------------------------------------")
                        fragments = {}
                        total_fragments = 0
                        connection_lost = False

                elif flag == TEXT | ACK:
                    self.acknowledged_event.set()


            except socket.timeout:
                if self.heartbeat_missed_count > 0:
                    connection_lost = True
                continue
            except OSError:
                if self.running:
                    print(end="")
                break

    def monitor_connection(self):
        while self.running:
            time.sleep(self.heartbeat_interval)
            if not self.running:
                break
            try:
                header = struct.pack(REZIA_HEDER_FORMAT, HRT)
                self.sock_send.sendto(header, (self.server_ip, self.server_port_receive))
                self.acknowledged_event_HRT.clear()
                if not self.acknowledged_event_HRT.wait(timeout=self.heartbeat_interval):
                    self.heartbeat_missed_count += 1
                    if self.heartbeat_missed_count >= self.max_missed_heartbeats:
                        self.running=False
                        self.quit()
                        break
            except OSError:
                break

    def quit(self):
        self.running = False
        self.sock_receive.close()
        self.sock_send.close()
        print("Client closing ....")


def run_client():
    global save_path
    ip_addr = input("Enter peer IP address:\n")
    port1 = int(input("Enter peer receive port:\n"))

    client_ip = "Localhost"
    client_port_recive = int(input("Enter port for reciving:\n"))
    save_path = input("Enter save path:\n")
    clinet_2_ip = ip_addr
    c2_port_recive = port1

    client = Client(client_ip, client_port_recive, clinet_2_ip, c2_port_recive)

    if client.local_port_sum > client.remote_port_sum:
        print("Local client initiating handshake...")
        initiate_thread = threading.Thread(target=client.initiate_handshake)
        initiate_thread.start()
        initiate_thread.join()
    else:
        print("Local client listening for handshake...")
        listen_thread = threading.Thread(target=client.listen_for_handshake)
        listen_thread.start()
        listen_thread.join()

    receive_thread = threading.Thread(target=client.receive_message)
    send_thread = threading.Thread(target=client.send_message)
    monitor_thread = threading.Thread(target=client.monitor_connection)
    receive_thread.start()
    send_thread.start()
    monitor_thread.start()
    send_thread.join()
    receive_thread.join()
    monitor_thread.join()


if __name__ == "__main__":
    client_thread = threading.Thread(target=run_client)
    client_thread.start()
    client_thread.join()
