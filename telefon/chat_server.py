# chat_server.py

import RPi.GPIO as GPIO
import time 
import sys
import socket
import select

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

ledPin1 = 23 # Broadcom pin 23 (P1 pin 16)
ledPin2 = 24 # Broadcom pin 23 (P1 pin 18)
ledPin3 = 25 # Broadcom pin 23 (P1 pin 22)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin1, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPin2, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPin3, GPIO.OUT) # LED pin set as output
#GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output

GPIO.output(ledPin1, GPIO.LOW)
GPIO.output(ledPin2, GPIO.LOW)
GPIO.output(ledPin3, GPIO.LOW)

            
def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)
 
    while 1:

        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
             
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                try:
                    # receiving data from the socket.
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # there is something in the socket
                        if data==1:
                            GPIO.output(ledPin2, GPIO.LOW)
                            GPIO.output(ledPin3, GPIO.LOW)
                            GPIO.output(ledPin1, GPIO.HIGH)
                            
                        elif data==2:
                            GPIO.output(ledPin1, GPIO.LOW)
                            GPIO.output(ledPin3, GPIO.LOW)
                            GPIO.output(ledPin2, GPIO.HIGH)
                            
                        elif data==3:
                            GPIO.output(ledPin2, GPIO.LOW)
                            GPIO.output(ledPin1, GPIO.LOW)
                            GPIO.output(ledPin3, GPIO.HIGH)
                            
                            
			#broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        # remove the socket that's broken    
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()
 
if __name__ == "__main__":

    sys.exit(chat_server())
