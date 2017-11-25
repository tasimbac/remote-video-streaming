import cv2
import numpy as np
import socket
import sys
import pickle
import struct

REMOTE_HOST_IP = '192.168.8.100'
REMOTE_PORT = 8081

#cap = cv2.VideoCapture(0)  #capture video from your webcam
cap = cv2.VideoCapture('dependency_injection.mp4')   #stream video content from local file
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((REMOTE_HOST_IP, REMOTE_PORT)) #connect to remote host 

while True:
    ret,frame = cap.read()
    data = pickle.dumps(frame)
    clientsocket.sendall(struct.pack("L", len(data)) + data) #send video to remote host