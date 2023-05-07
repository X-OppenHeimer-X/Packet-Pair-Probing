# Packet-Pair-Probing

## Effect of Cross-traffic on Packet Pair Probing

This repository contains the code for the final project for CS553: Design of Internet Services at Rutgers University.

## Authors

- Toshitt Ahuja
- Jodh Singh


This Readme file carries the step-by-step instructions to recreate the experiments in our project.


## Requirements
1. Ubuntu(PC or Virtual Machine) 22.04/20.04 (preferably 22.04)
2. Mininet (Learn to install mininet on your system [here](https://www.youtube.com/watch?v=ZUzHKDIUFh4))
3. Python 3.10 or above
4. Numpy (version 1.21.5)
5. Matplotlib(version 3.5.1)





## Constant Bandwidth Experiments

### i. Without Cross Traffic

Set up the following configurations the `config.py` file:

```python

CROSS_TRAFFIC = False

FIXED_BANDWIDTH = True

FIXED_PACKET_SIZE = False

```

Remember, you can change the values and sizes `sizes` and `bandwidths` in the `config.py` file, considering they are of the same size.

Start the network on your system by running the `ppp_main.py` file.

```shell
sudo python3 ppp_main.py
```

To setup the server, run the `ppp_server.py file`

```shell
sudo python3 ppp_server.py
```

Once the server starts, run the `ppp_client_fixed_bandwith.py file`

```shell
sudo python3 ppp_client_fixed_bandwith.py
```

You will now have fully generated pickle files, consisting of the list of  `initial_dispersion` and `final_dispersion`

To generate the plots run the `plots.py` file.

```shell
sudo python3 plots.py
```

Once the plots are generated, feel free to delete the pickle files.

> **Warning**
> 
> To reinitiate this experiment, delete the pickle files for veritable results

---

### ii. With Cross Traffic

Set up the following configurations the `config.py` file:

```python

CROSS_TRAFFIC = True

FIXED_BANDWIDTH = True

FIXED_PACKET_SIZE = False

```

Remember, you can change the values and sizes `sizes` and `bandwidths` in the `config.py` file, considering they are of the same size.

Start the network on your system by running the `ppp_main.py` file.

```shell
sudo python3 ppp_main.py
```

Once you run the command, xterm terminals of `h1`, `h2`, `h3` and `h4` pop up.

To run cross traffic from h3 to h4:

Turn `h4` into server by running :

```shell
iperf -s -u
```
Once done, start generating UDP cross traffic from `h3` by running:

```shell
iperf -c 192.168.4.2 -b {bandwidth}M -u -t 10000
```



To setup the server, run the `ppp_server.py file`

```shell
sudo python3 ppp_server.py
```

Once the server starts, run the `ppp_client_fixed_bandwith.py file`

```shell
sudo python3 ppp_client_fixed_bandwith.py
```

You will now have fully generated pickle files, consisting of the list of  `initial_dispersion` and `final_dispersion`.Once the pickle files are generated,
stop the iperf traffic.

To generate the plots run the `plots.py` file.

```shell
sudo python3 plots.py
```

Once the plots are generated, feel free to delete the pickle files.

> **Warning**
> 
> To reinitiate this experiment, delete the pickle files for veritable results

---


## Constant Packet-size Experiments

### i. Without Cross Traffic

Set up the following configurations the `config.py` file:

```python

CROSS_TRAFFIC = False

FIXED_BANDWIDTH = False

FIXED_PACKET_SIZE = True

```

Remember, you can change the values and sizes `sizes` and `bandwidths` in the `config.py` file, considering they are of the same size.

Start the network on your system by running the `ppp_main.py` file.

```shell
sudo python3 ppp_main.py
```

To setup the server, run the `ppp_server.py file`

```shell
sudo python3 ppp_server.py
```

Once the server starts, run the `ppp_client_fixed_bandwith.py file`

```shell
sudo python3 ppp_client_fixed_bandwith.py
```

Repeat these steps over and over for different bandwidths(preferably from `bandwidths`) till you get your desired number of samples.


Once done,to generate the plots run the `plots.py` file.

```shell
sudo python3 plots.py
```

Once the plots are generated, feel free to delete the pickle files.

> **Warning**
> 
> To reinitiate this experiment, delete the pickle files for veritable results

---


### ii. With Cross Traffic

Set up the following configurations the `config.py` file:

```python

CROSS_TRAFFIC = True

FIXED_BANDWIDTH = False

FIXED_PACKET_SIZE = True

```

Remember, you can change the values and sizes `sizes` and `bandwidths` in the `config.py` file, considering they are of the same size.

Start the network on your system by running the `ppp_main.py` file.

```shell
sudo python3 ppp_main.py
```

Once you run the command, xterm terminals of `h1`, `h2`, `h3` and `h4` pop up.

To run cross traffic from h3 to h4:

Turn `h4` into server by running :

```shell
iperf -s -u
```
Once done, start generating UDP cross traffic from `h3` by running:

```shell
iperf -c 192.168.4.2 -b {bandwidth}M -u -t 10000
```



To setup the server, run the `ppp_server.py file`

```shell
sudo python3 ppp_server.py
```

Once the server starts, run the `ppp_client_fixed_bandwith.py file`

```shell
sudo python3 ppp_client_fixed_bandwith.py
```

Repeat these steps over and over for different bandwidths(preferably from `bandwidths`) till you get your desired number of samples.


Once done,to generate the plots run the `plots.py` file.

```shell
sudo python3 plots.py
```

Once the plots are generated, feel free to delete the pickle files.

> **Warning**
> 
> To reinitiate this experiment, delete the pickle files for veritable results


