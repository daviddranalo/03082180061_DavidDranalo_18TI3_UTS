import socket

s = socket.socket()
host = socket.gethostname()
port = 8800
s.bind((host,port))
s.listen(1)
print(host)
print("Menunggu konensi......")
conn, addr = s.accept()
print(addr, "sudah terkoneksi dengan server")

filename=input(str("silahkan masukan nama file yang akan di kirim: "))
file = open(filename,'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data sudah berhasil di kirim")
print (" Terima kasih :) ")
