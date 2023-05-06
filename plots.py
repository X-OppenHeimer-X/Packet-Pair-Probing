import matplotlib.pyplot as plt
import numpy as np
import config as c
import pickle as pkl
import sys
import datetime
from config import bandwidths,packet_size

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

if c.FIXED_BANDWIDTH == True:

    with open("initial_dispersion_fixed_bw.pkl","rb") as f:
        dispersion_list_initial = pkl.load(f)

    with open("final_dispersion_fixed_bw.pkl","rb") as f:
        dispersion_list_final = pkl.load(f)

    if c.CROSS_TRAFFIC == False:
        fig, ax = plt.subplots()
        ax.scatter(c.sizes, dispersion_list_initial, label='Dispersion_in')
        ax.scatter(c.sizes, dispersion_list_final,label='Dispersion_out')
        ax.set_title(f'Initial and Final Dispersion for bandwidth: {c.bandwidth}')
        ax.set_xlabel('Packet Size')
        ax.set_ylabel('Dispersion')
        ax.legend()
        plt.savefig(f'./plot_directory/fixed_bandwidth_size/no_cross_traffic/dispersion_{c.bandwidth}_mbit_sec_{timestamp}.jpg')
               

    else:
        fig, ax = plt.subplots()
        ax.scatter(c.sizes, dispersion_list_initial, label='Dispersion_in')
        ax.scatter(c.sizes, dispersion_list_final,label='Dispersion_out')
        ax.set_title(f'Initial and Final Dispersion for bandwidth {c.bandwidth}')
        ax.set_xlabel('Packet Size')
        ax.set_ylabel('Dispersion')
        ax.legend()
        plt.savefig(f'./plot_directory/fixed_bandwidth_size/with_cross_traffic/CT_dispersion_{c.bandwidth}_mbit_sec_{timestamp}.jpg')

else:
    with open("initial_dispersions_fixed_ps.pkl","rb") as f:
        dispersion_list_initial = pkl.load(f)

    with open("final_dispersion_fixed_ps.pkl","rb") as f:
        dispersion_list_final = pkl.load(f)


    if c.CROSS_TRAFFIC == False:
        
        fig, ax = plt.subplots()
        ax.scatter(c.bandwidths, dispersion_list_initial, label='Dispersion_in')
        ax.scatter(c.bandwidths, dispersion_list_final,label='Dispersion_out')
        ax.set_title(f'Initial and Final Dispersion for packet size')
        ax.set_xlabel('Bandwidth')
        ax.set_ylabel('Dispersion')
        ax.legend()
        plt.savefig(f'./plot_directory/fixed_packet_size/no_cross_traffic/dispersion_{packet_size}_bytes_{timestamp}.jpg')
    else:
        fig, ax = plt.subplots()
        ax.scatter(c.bandwidths, dispersion_list_initial, label='Dispersion_in')
        ax.scatter(c.bandwidths, dispersion_list_final,label='Dispersion_out')
        ax.set_title(f'Initial and Final Dispersion for packet size')
        ax.set_xlabel('Bandwidth')
        ax.set_ylabel('Dispersion')
        ax.legend()
        plt.savefig(f'./plot_directory/fixed_packet_size/with_cross_traffic/dispersion_{packet_size}_bytes_{timestamp}.jpg')




