import numpy as np
from scipy.stats import skew, kurtosis

def extract_features(data):
    feature_vector = []
    for i in range(6):
        channel_data = data[:, i]
        f_mean = np.mean(channel_data)
        f_std = np.std(channel_data)
        f_range = np.max(channel_data) - np.min(channel_data)
        f_rms = np.sqrt(np.mean(np.square(channel_data)))

        fft_values = np.abs(np.fft.rfft(channel_data))

        f_energy = np.sum(np.square(fft_values))
        f_dom_freq = np.argmax(fft_values)
        f_skew = skew(fft_values)
        f_kurtosis = kurtosis(fft_values)

        feature_vector.extend([f_mean, f_std, f_range, f_rms, f_energy, f_dom_freq, f_skew, f_kurtosis])

    return np.array(feature_vector)