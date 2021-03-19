import socket

s = socket.socket()
host = input(str("Masukkan alamat host: "))
port = 8800
s.connect((host,port))
print("Terkoneksi......")

filename=input(str("silahkan masukan nama file akan di letak: "))
file = open (filename,'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("Data sudah berhasil di simpan")
print (" Terima kasih :) ")
               
