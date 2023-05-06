import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import config as c
from config import initial_dispersion_list_fixed_packet_size
import pickle as pkl


pickle_file = "initial_dispersions_fixed_ps.pkl"

if os.path.isfile(pickle_file) == True:
    with open(pickle_file,"rb") as f:
        initial_dispersion_list_fixed_packet_size = pkl.load(f)
else:
    with open(pickle_file,"wb") as f:
        pkl.dump(initial_dispersion_list_fixed_packet_size,f)



## The list of varying 
    
# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



# server_address = ('localhost', 5000)
server_address = ('192.168.1.2', 12346)


# send a message to the server

packet1 = b'x\00'
packet2 = b'x\01'


start_time_p1 = time.time()
client_socket.sendto(packet1, server_address)
start_time_p2 = time.time()
client_socket.sendto(packet2, server_address)
initial_dispersion = abs(start_time_p1 - start_time_p2)
initial_dispersion_list_fixed_packet_size.append(initial_dispersion)
with open(pickle_file,"wb") as f:
    pkl.dump(initial_dispersion_list_fixed_packet_size,f)
print(f'(without Cross Traffic) Initial Dispersion is : {initial_dispersion}')








