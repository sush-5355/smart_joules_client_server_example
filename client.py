import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1089))

msg = s.recv(1024)
while msg:

    print('recieved ' + msg.decode('utf-8'))
    msg = s.recv(1024)
s.close()
