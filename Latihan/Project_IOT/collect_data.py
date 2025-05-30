import serial
import numpy as np
import os
import time
from datetime import datetime
import serial.tools.list_ports

def record_sample(ser, label, sample_number):
    """Record one audio sample and save it with proper labeling."""
    samples = []
    
    # Flush any existing data
    ser.reset_input_buffer()
    
    # Send record command
    ser.write(b'R')
    
    # Create directory if it doesn't exist
    os.makedirs(f'data/{label}', exist_ok=True)
    
    # Read samples until END marker
    while True:
        try:
            line = ser.readline()
            try:
                decoded_line = line.decode('ascii').strip()
                if decoded_line == "END":
                    break
                if decoded_line:  # Only process non-empty lines
                    try:
                        sample = int(decoded_line)
                        samples.append(sample)
                    except ValueError:
                        continue
            except UnicodeDecodeError:
                continue
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            break
    
    if len(samples) > 0:
        # Save the sample
        filename = f'data/{label}/sample_{sample_number}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.npy'
        np.save(filename, np.array(samples))
        print(f"Recorded {len(samples)} samples")
        return filename
    else:
        print("No samples recorded!")
        return None

def collect_dataset(serial_port, baud_rate=115200):
    """Collect a complete dataset with multiple samples per label."""
    try:
        ser = serial.Serial(
            port=serial_port,
            baudrate=baud_rate,
            timeout=2,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE
        )
        
        time.sleep(2)  # Wait for connection to establish
        print("Serial connection established")
        
        # Hanya mengumpulkan allahu_akbar dan subhanallah
        labels = ["allahu_akbar", "subhanallah"]
        samples_per_label = 20  # Mengurangi jumlah sampel
        
        try:
            for label in labels:
                print(f"\nRecording samples for: {label}")
                print("Get ready to speak...")
                for i in range(samples_per_label):
                    input(f"Press Enter to record sample {i+1}/{samples_per_label} for {label}...")
                    print("Recording...")
                    filename = record_sample(ser, label, i)
                    if filename:
                        print(f"Saved: {filename}")
                    else:
                        print("Failed to record sample, trying again...")
                        continue
                    print("Wait for 1 second before next recording...")
                    time.sleep(1)
                print(f"Completed recording for {label}")
                    
        finally:
            ser.close()
            print("Serial connection closed")
            
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        available_ports = list(serial.tools.list_ports.comports())
        if available_ports:
            print("\nAvailable ports:")
            for p in available_ports:
                print(f"- {p.device}: {p.description}")
        else:
            print("No serial ports found!")

def list_ports():
    """List all available serial ports."""
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No serial ports found!")
        return None
        
    print("\nAvailable COM ports:")
    for i, p in enumerate(ports):
        print(f"{i}: {p.device} - {p.description}")
    return ports

if __name__ == "__main__":
    try:
        ports = list_ports()
        if not ports:
            exit(1)
            
        port_index = int(input("\nSelect port number: "))
        if port_index < 0 or port_index >= len(ports):
            print("Invalid port number!")
            exit(1)
            
        selected_port = ports[port_index].device
        print(f"\nUsing port: {selected_port}")
        
        collect_dataset(selected_port, baud_rate=115200)
        
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure ESP32 is properly connected")
        print("2. Close Arduino IDE and any other serial monitors")
        print("3. Check if the correct port is selected")
        print("4. Try unplugging and reconnecting the ESP32")