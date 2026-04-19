import pandas as pd
import numpy as np
import os 

def k_load_raw_iot_signals(base_path, subset):
        
    k_signal_dir = os.path.join(base_path, subset , 'Inertial Signals')
  
    files = [
        f'total_acc_x_{subset}.txt', f'total_acc_y_{subset}.txt', f'total_acc_z_{subset}.txt',
        f'body_gyro_x_{subset}.txt', f'body_gyro_y_{subset}.txt', f'body_gyro_z_{subset}.txt'
    ]

    data_list = []
    for file in files:
        full_path = os.path.join(k_signal_dir, file)
        channel_data = np.loadtxt(full_path)
        data_list.append(channel_data)
    return np.transpose(np.array(data_list), (1, 2, 0))

PATH = r"datasets\Kinetic\UCI HAR Dataset"

kX_train = k_load_raw_iot_signals(PATH, 'train')
kX_test = k_load_raw_iot_signals(PATH, 'test')
print(kX_train.shape, kX_test.shape)
