import socket


class CheckAdapter:
    def __init__(self, addr, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr
        self.port = port

    def say_server(self, user_id, sending_id):
        try:
            self.sock.connect((self.addr, self.port))
            data = 'sending ' + str(user_id) + ' ' + str(sending_id)
            self.sock.send(data.encode('utf-8'))
            self.sock.close()
            return 'Ok'
        except Exception:
            return 'Error'
