from config import CONFIG
from testing_thread import TestingThread
from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind((gethostbyname('localhost'), 65500))
tcp_socket.listen(100)

while True:
    # try:
        connect = tcp_socket.accept()  # Get connect with user
        TestingThread(CONFIG, connect[0]).start()  # Run testing Thread
    # except Exception:
    #    print('Something went wrong')
