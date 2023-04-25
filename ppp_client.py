import socket
import time

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set the server address and port
server_address = ('10.0.0.2', 5500)

# send a message to the server
packet1 = b'x\00'*100
packet2 = b'x\01'*100

start_time_p1 = time.time()
client_socket.sendto(packet1, server_address)
start_time_p2 = time.time()
client_socket.sendto(packet2, server_address)
print(f'Dispersion in: {abs(start_time_p1 - start_time_p2)}')

response, _ = client_socket.recvfrom(1024)
end_time_p1 = time.time()
print(f'Received response from server: {response.decode()}')
print(f"One way time: {(end_time_p1 - start_time_p1)/2}")

response, _ = client_socket.recvfrom(1024)
end_time_p2 = time.time()
print(f'Received response from server: {response.decode()}')
print(f"One way time: {(end_time_p2 - start_time_p2)/2}")



# receive a response from the server
# print the response

