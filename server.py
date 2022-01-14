import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1089))
s.listen(1024)
while True:
    clt , adr = s.accept()
    print(f'Connection to {adr} established')
    clt.send(bytes('Socket Program ','utf-8'))
    msg = 'bye.....'
    clt.send(msg.encode())
    msg1 = "mkdir I:\Python Projects\socket programing"
    clt.send(msg1.encode())
    f = open("myfile.txt", "w")
    clt.send(f.encode())
    clt.close()