import socket
from _socket import SHUT_WR

def main():
    host = '127.0.0.1'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    with open("test.mp3", "rb") as f:
        sock.sendfile(f)

    sock.shutdown(SHUT_WR)

    with open("returned.mp3", "wb") as f:
        while True:
            l = sock.recv(500)
            if not l:
                break
            f.write(l)
    sock.close()

if __name__ == "__main__":
    main()
