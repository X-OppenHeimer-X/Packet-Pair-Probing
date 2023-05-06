#Note: Please make sure FIXED_BANDWIDTH and FIXEDexit
# _PACKET_SIZE aren't True or False altogether.

CROSS_TRAFFIC = False

FIXED_BANDWIDTH = True

FIXED_PACKET_SIZE = False

sizes = [3500, 4000, 4500, 5000, 5500, 6000, 7500, 8000, 9000]

bandwidth = 20

packet_size = 20000 #bytes

bandwidths = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]



##These values inside these lists must not be touched by the user. 

initial_dispersion_fb = 0
initial_dispersion_list_fixed_bandwidth = []

final_dispersions_list_fixed_bandwidth = []


initial_dispersion_list_fixed_packet_size = []

final_dispersions_list_fixed_packet_size = []
