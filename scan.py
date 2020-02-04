import socket
import time


startTime = time.time()

targetIP = input('Enter the host to scan: ')
t_IP = socket.gethostbyname(targetIP)

print ('Starting host: ', t_IP)

for i in range (50,500):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        connect = s.connect_ex((t_IP,i))

if (connect == 0):
        print ('Port %d: OPEN' % (i,))

s.close()

print('Time taken:', time.time() - startTime)

