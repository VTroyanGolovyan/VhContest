from config import CONFIG
from testing_thread import TestingThread
from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind((gethostbyname('localhost'), 5555))
tcp_socket.listen(1000)

while True:
    connect = tcp_socket.accept()
    TestingThread(CONFIG, connect).start()
