import socket
import pickle
from _thread import *

from player import Player

server = '192.168.1.146'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print('waiting for connection, Server Started')


players = [Player(0, 0, 50, 50, (0, 255, 0)),
           Player(100, 100, 50, 50, (255, 0, 0))]


def client(conn, player):  # threaded function
    conn.send(pickle.dumps(players[player]))
    reply = ''

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print('disconnected')
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print('Received:', data)
                print('Sending:', reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print('Connection lost')
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print('Connected to:', addr)

    start_new_thread(client, (conn, current_player))
    current_player += 1
