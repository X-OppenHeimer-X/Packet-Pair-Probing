import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a public host and a port
server_socket.bind(('10.0.0.2', 5500))

# wait for incoming datagrams
print('Server listening on port 5500...')
while True:
    # receive data from client
    data, address = server_socket.recvfrom(1024)
    # print the received data and client address
    response = "Received Thanks"
    server_socket.sendto(response.encode(),address)
    print(f'Received data from {address}: {data}')
    

