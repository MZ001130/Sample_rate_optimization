import pandas as pd
import numpy as np
import os 

def load_kinetic_csv(train_path, test_path): 
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    y_train = train_df['Activity']
    X_train = traind_df.drop(['Activity', 'subject'], axis=1, errors='ignore')

    y_test = test_df['Activity']
    X_test = test_df.drop(['Activity', 'subject'], axis=1, errors='ignore')

    return X_train, y_train, X_test, y_test

kinetic_train_csv = "C:\Users\moham\Documents\GitHub\Sample_rate_optimization\datasets\Kinetic\train.csv"
kinetic_test_csv = "C:\Users\moham\Documents\GitHub\Sample_rate_optimization\datasets\Kinetic\test.csv"

kX_train, ky_train, kX_test, ky_test = load_kinetic_csv(kinetic_train_csv, kinetic_test_csv)

print(f"Training data shape: {kX_train.shape}")
print(f"Unique Activities: {ky_train.unique()}")