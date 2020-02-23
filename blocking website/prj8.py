#  security
#to secure data we must secure ports were all data transfer is done
#socket library is used fo this operation
#AF_INET is used for ping port
#SOCK_STREAM is used for lower port



import socket

remoteServer=input("Enter the port to scan")

for port in range(0,9000):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # this will scan
    result=sock.connect_ex((remoteServer,port))           # this will check the connectivity
    if result==0:
        print("Port{}:open".format(port))                   #if port is not in used
    else:
        print("Port{}:Close".format(port))                  #if port is in used
    sock.close()



