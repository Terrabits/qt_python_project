import socket


class Model:
    def __init__(self):
        self.socket = None

    # properties ("things")

    @property
    def id_string(self):
        assert self.socket
        self.socket.sendall(b'*IDN?\n')
        return self.socket.recv(1024).strip().decode()

    @property
    def connected(self):
        # assume connected if socket
        return bool(self.socket)

    # methods ("actions")

    def connect(self, address, port=5025):
        assert not self.connected
        try:
            self.socket = socket.socket()
            self.socket.connect((address, port))
            return True
        except Exception:
            self.socket = None
            return False

    def disconnect(self):
        assert self.connected
        try:
            self.socket.close()
        except Exception:
            pass
        # delete socket
        self.socket = None
