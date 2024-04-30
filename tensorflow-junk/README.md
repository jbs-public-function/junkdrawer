# Tensorflow

### nvidia-smi output
```shell
tensorflow ❯ nvidia-smi
Mon Apr 29 21:21:05 2024       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.67                 Driver Version: 550.67         CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 ...    Off |   00000000:01:00.0  On |                  N/A |
|  0%   32C    P8             12W /  285W |     765MiB /  16376MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      2584      G   /usr/lib/xorg/Xorg                            337MiB |
|    0   N/A  N/A      2854      G   /usr/bin/gnome-shell                           74MiB |
|    0   N/A  N/A      3660      G   ...irefox/4173/usr/lib/firefox/firefox        164MiB |
|    0   N/A  N/A      6279      G   ...erProcess --variations-seed-version         77MiB |
+-----------------------------------------------------------------------------------------+
```

### installing in venv
I have cudnn version 9.1 installed. This isn't really supported by tensorflow yet on Ubuntu or I need to build from source etc, but this solution seems to work
https://stackoverflow.com/questions/77467690/tensorflow-version-for-cuda-12-2-1
```shell
# activate .venv
$ source .venv/bin/activate

# install tensorflow
pip install "tensorflow[and-cuda]==2.16.1"

# set LD_LIBRARY_PATH
# no idea why this works
export LD_LIBRARY_PATH=.venv/lib/python3.10/site-packages/nvidia/cudnn/lib/:$LD_LIBRARY_PATH
```

### Docker
install nvidia-toolkit

nvidia repository

https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow

image -`nvcr.io/nvidia/tensorflow:24.04-tf2-py3`