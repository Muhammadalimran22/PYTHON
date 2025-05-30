# check_data.py
import os
import numpy as np

def check_data():
    data_dir = 'data'
    for label in os.listdir(data_dir):
        label_path = os.path.join(data_dir, label)
        if os.path.isdir(label_path):
            files = [f for f in os.listdir(label_path) if f.endswith('.npy')]
            print(f"\nLabel: {label}")
            print(f"Number of samples: {len(files)}")
            if files:
                # Check first file shape
                sample = np.load(os.path.join(label_path, files[0]))
                print(f"Sample shape: {sample.shape}")

if __name__ == "__main__":
    check_data()