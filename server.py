import socket
import sys
import cv2
import pickle
import numpy as np
import struct

#ip and port address of machine hosting the server.py application
MY_IP = '192.168.0.70'
MY_PORT = 8081
#socket where server application will be listening to as it waits for client app to make connection request
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
# bind socket to the port number
s.bind((MY_IP, MY_PORT))
print('Socket bind complete')
#socket refresh/listening interval
s.listen(10)
print('Socket now listening')

conn, addr = s.accept()

#data received from socket will be stored as bytes
data = b''
payload_size = struct.calcsize("L")

while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]

    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame=pickle.loads(frame_data)
    #print (frame.size)  #print frame size
    cv2.imshow('frame', frame)  #show frames in opencv window
    cv2.waitKey(10) #interval in ms to refresh frames. should be used only if you are showing frames in gui