import socket
import time 
import config as c
import pickle as pkl
import os
from config import final_dispersions_list_fixed_packet_size, final_dispersions_list_fixed_bandwidth,bandwidth,initial_dispersion_fb
import sys

if c.FIXED_BANDWIDTH == True and c.FIXED_PACKET_SIZE == False:
    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind the socket to a public host and a port
    server_socket.bind(('192.168.1.2', 12346))


    print('Server listening on port 5500...')
    # while True:
    #     # receive data from client
    trials = len(c.sizes)
    trial_number = 0
    while True and trial_number < trials:    
        packet_1, client_address = server_socket.recvfrom(1024)
        packet1_receiving_time = time.time()
        packet1_receiving_time = packet1_receiving_time + (c.sizes[trial_number]/c.bandwidth)
        print(f"Packet 1 for trial number #{trial_number+1} received")
        packet_2, client_address = server_socket.recvfrom(1024)
        packet2_receiving_time = time.time()
        packet2_receiving_time = packet2_receiving_time + (c.sizes[trial_number]/c.bandwidth)
        print(f"Packet 2 for trial number #{trial_number+1} received")
        final_dispersions_list_fixed_bandwidth.append(packet2_receiving_time - packet1_receiving_time) 
        trial_number+=1
        


    with open("final_dispersion_fixed_bw.pkl","wb") as f:
        pkl.dump(final_dispersions_list_fixed_bandwidth,f)


elif c.FIXED_BANDWIDTH == False and c.FIXED_PACKET_SIZE == True:
    if os.path.isfile('final_dispersion_fixed_ps.pkl'):
        with open("final_dispersion_fixed_ps.pkl","rb") as f:
            final_dispersions_list_fixed_packet_size = pkl.load(f)
    else:
        with open("final_dispersion_fixed_ps.pkl","wb") as f:
            pkl.dump(final_dispersions_list_fixed_packet_size,f)

    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind the socket to a public host and a port
    server_socket.bind(('192.168.1.2', 12346))


    print('Server listening on port 5500...')
    # while True:
    #     # receive data from client
    trial_number = 0
    while True and trial_number<1:    
        packet_1, client_address = server_socket.recvfrom(1024)
        packet1_receiving_time = time.time()
        print(f"Packet 1 for trial number #{trial_number+1} for bandwidth {bandwidth}Mbits/sec received")
        packet_2, client_address = server_socket.recvfrom(1024)
        packet2_receiving_time = time.time()
        print(f"Packet 2 for trial number #{trial_number+1} for bandwidth {bandwidth}Mbits/sec received")
        final_dispersions_list_fixed_packet_size.append(max(c.packet_size/(bandwidth*1000000),(packet2_receiving_time - packet1_receiving_time)))
        trial_number+=1

    with open("final_dispersion_fixed_ps.pkl","wb") as f:
        pkl.dump(final_dispersions_list_fixed_packet_size,f)
    
else:
    print("The configuration is incorrect.Please fix the configuration in config.py file")
    sys.exit()