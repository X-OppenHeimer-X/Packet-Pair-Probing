#Important instructions: 

#1. Please make sure FIXED_BANDWIDTH and FIXED_PACKET_SIZE aren't True or False altogether.
#2. Make sure 'sizes' and 'bandwidths' lists are of the same length.

##Changeable values

CROSS_TRAFFIC = True

FIXED_BANDWIDTH = False

FIXED_PACKET_SIZE = True


sizes = [3500,3750,4000,4250,5000,5500,6000,7500]

bandwidth = 55

packet_size = 20000 #bytes

bandwidths = [20, 25, 30, 35, 40, 45, 50, 55]




##These values inside these lists and variables must not be touched by the user here.

initial_dispersion_fb = 0

initial_dispersion_list_fixed_bandwidth = []

final_dispersions_list_fixed_bandwidth = []

initial_dispersion_list_fixed_packet_size = []

final_dispersions_list_fixed_packet_size = []
