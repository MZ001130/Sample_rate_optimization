import os
import numpy as np
from load_data import k_load_raw_iot_signals
from decimator import butterworth_decimation
from feature_extraction import extract_features

PATH = r"datasets\Kinetic\UCI HAR Dataset"
kX_train = k_load_raw_iot_signals(PATH, 'train')


original_fs = 50
target_fs = 10

sample_window = kX_train[0]
downsampled_window = butterworth_decimation(sample_window, original_fs, target_fs)
print("Original shape:", sample_window.shape[0])
print("Downsampled shape:", downsampled_window.shape[0])

feature_50hz = extract_features(sample_window)
feature_10hz = extract_features(downsampled_window)
print("Feature vector at 50 Hz:", feature_50hz)
print("Feature vector at 10 Hz:", feature_10hz)
print("\nComparison of feature vectors:")
print("50ZH features:", feature_50hz[:3])
print("10HZ features:", feature_10hz[:3])
