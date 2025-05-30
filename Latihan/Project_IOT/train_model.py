import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

def prepare_dataset():
    """Load and prepare the dataset for training."""
    X = []
    y = []
    
    print("Loading dataset...")
    data_dir = 'data'
    if not os.path.exists(data_dir):
        raise Exception(f"Directory {data_dir} not found! Please run data collection first.")
    
    # Load all samples from data directory
    for label in os.listdir(data_dir):
        label_path = os.path.join(data_dir, label)
        if os.path.isdir(label_path):
            print(f"Processing {label} samples...")
            for sample_file in os.listdir(label_path):
                if sample_file.endswith('.npy'):
                    sample_path = os.path.join(label_path, sample_file)
                    try:
                        sample = np.load(sample_path)
                        features = extract_features(sample)
                        
                        # Debug information
                        print(f"Sample shape: {sample.shape}, Features shape: {features.shape}")
                        
                        X.append(features)
                        y.append(label)
                    except Exception as e:
                        print(f"Error loading {sample_path}: {e}")
                        continue
    
    if not X:
        raise Exception("No data found! Please run data collection first.")
    
    X = np.array(X)
    y = np.array(y)
    
    print(f"Final X shape: {X.shape}")
    print(f"Final y shape: {y.shape}")
    
    # Encode labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Save label encoder for later use
    np.save('label_encoder_classes.npy', le.classes_)
    
    print(f"Dataset prepared: {X.shape[0]} samples, {len(np.unique(y))} classes")
    return train_test_split(X, y_encoded, test_size=0.2, random_state=42)

def extract_features(audio_data):
    """Extract relevant features from raw audio data."""
    # Ensure audio_data is 1D
    audio_data = audio_data.flatten()
    
    # Normalize
    audio_normalized = (audio_data - np.mean(audio_data)) / np.std(audio_data)
    
    # Calculate FFT
    fft_features = np.abs(np.fft.rfft(audio_normalized))
    
    # Ensure consistent feature length
    n_features = 1000  # Fixed number of features
    
    if len(fft_features) > n_features:
        fft_features = fft_features[:n_features]
    else:
        # Pad with zeros if too short
        fft_features = np.pad(fft_features, (0, n_features - len(fft_features)))
    
    # Add more features
    zero_crossings = np.sum(np.abs(np.diff(np.signbit(audio_normalized)))) / len(audio_normalized)
    energy = np.sum(audio_normalized ** 2) / len(audio_normalized)
    
    # Combine all features
    features = np.concatenate([
        fft_features,
        np.array([zero_crossings, energy])
    ])
    
    return features

def create_model(input_shape, num_classes):
    """Create and return the neural network model."""
    print(f"Creating model with input shape: {input_shape}, num_classes: {num_classes}")
    
    model = tf.keras.Sequential([
        layers.Input(shape=(input_shape,)),  # Note the change here
        layers.BatchNormalization(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    return model

def train():
    """Train the model on collected dataset."""
    try:
        # Prepare data
        X_train, X_test, y_train, y_test = prepare_dataset()
        
        print(f"Training data shape: {X_train.shape}")
        print(f"Test data shape: {X_test.shape}")
        
        # Create and compile model
        model = create_model(X_train.shape[1], len(np.unique(y_train)))
        
        # Model summary
        model.summary()
        
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        # Train
        print("\nStarting training...")
        history = model.fit(
            X_train, y_train,
            validation_data=(X_test, y_test),
            epochs=50,
            batch_size=32,
            verbose=1
        )
        
        # Evaluate model
        print("\nEvaluating model...")
        test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
        print(f"Test accuracy: {test_accuracy*100:.2f}%")
        
        # Save model
        model.save('sound_recognition_model.keras')
        print("\nModel saved as 'sound_recognition_model'")
        
        return history, model
        
    except Exception as e:
        print(f"Error during training: {e}")
        print("Stack trace:")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    try:
        print("TensorFlow version:", tf.__version__)
        history, model = train()
        print("Training completed successfully!")
    except Exception as e:
        print(f"Training failed: {e}")