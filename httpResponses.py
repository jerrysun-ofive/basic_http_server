"""
 Implements a simple HTTP/1.0 Server

"""

import socket

# defining socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# AF = address family -> used to designate the type of addresses that the socket
# can communicate with (in this case, Internet Protocol v4 addresses)
# SOCK_STREAM -> TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print("Listening on port %s ..." % SERVER_PORT)

while True:
    # wait for client connections
    client_connection, client_address = server_socket.accept()

    # get the client request
    request = client_connection.recv(1024).decode()
    print(request)
    
    # sent HTTP response
    response = 'HTTP/1.0 200 OK\n\nHello World'
    client_connection.sendall(response.encode())
    client_connection.close()

# close the socket
server_socket.close()



## resources used ##
# https://stackoverflow.com/questions/1593946/what-is-af-inet-and-why-do-i-need-it 
