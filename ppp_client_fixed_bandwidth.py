import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import pickle as pkl
import config as c
import struct
from config import initial_dispersion_list_fixed_bandwidth,initial_dispersion_fb
    
# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# server_address = ('localhost', 5000)
server_address = ('192.168.1.2', 12346)


# send a message to the server

packet1 = struct.pack('b', 0)   ##creates packets of one byte each
  ##byte packets
packet2 = struct.pack('b', 1)

##created a tuple of pair of packets 

trials = len(c.sizes) ##number of samples.
list_of_packet_pairs = [(packet1*size,packet2*size) for size in c.sizes]


if c.CROSS_TRAFFIC == True:
    for pair in list_of_packet_pairs:

        pkt1 = pair[0]
        pkt2 = pair[1]
        time.sleep(2)
        client_socket.sendto(pkt1, server_address)
        start_time_pkt1 = time.time()

        client_socket.sendto(pkt2, server_address)
        start_time_pkt2 = time.time()

        initial_dispersion = abs(start_time_pkt1 - start_time_pkt2)
        initial_dispersion_list_fixed_bandwidth.append(initial_dispersion)
        # initial_dispersion_fb = initial_dispersion
        # time.sleep(2)
        print(f'(CT == FALSE) Initial Dispersion for packet-size {c.sizes[list_of_packet_pairs.index(pair)]} : {initial_dispersion}')


else:
    for pair in list_of_packet_pairs:

        pkt1 = pair[0]
        pkt2 = pair[1]

        start_time_pkt1 = time.time()
        client_socket.sendto(pkt1, server_address)
        start_time_pkt2 = time.time()
        client_socket.sendto(pkt2, server_address)

        initial_dispersion = abs(start_time_pkt1 - start_time_pkt2)
        initial_dispersion_list_fixed_bandwidth.append(initial_dispersion)
        print(f'(CT == FALSE) Initial Dispersion for packet-size {c.sizes[list_of_packet_pairs.index(pair)]} : {initial_dispersion}')

##saving the changes to initital_dispersion_list at modular level.

with open("initial_dispersion_fixed_bw.pkl","wb") as f:
    pkl.dump(initial_dispersion_list_fixed_bandwidth,f)

    


