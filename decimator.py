from scipy.signal import butter, lfilter
from load_data import k_load_raw_iot_signals


def butterworth_decimation(data, original_fs, target_fs, order=4):
   
    if target_fs >= original_fs:
        return data
    

    nyquist = 0.5 * original_fs
    cutoff = 0.5 * target_fs / nyquist
    b, a = butter(order, cutoff, btype='low')

    filtered_data = lfilter(b, a, data, axis=0)

    step = int(original_fs / target_fs)
    decimated_data = filtered_data[::step]

    return decimated_data


