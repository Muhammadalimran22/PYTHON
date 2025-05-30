# import serial
# import numpy as np
# import tensorflow as tf
# import serial.tools.list_ports

# def list_ports():
#     """Menampilkan semua port serial yang tersedia"""
#     ports = list(serial.tools.list_ports.comports())
#     if not ports:
#         print("Tidak ada port serial ditemukan!")
#         return None
        
#     print("\nPort COM yang tersedia:")
#     for i, p in enumerate(ports):
#         print(f"{i}: {p.device} - {p.description}")
#     return ports

# def main():
#     # Load model
#     print("Loading model...")
#     model = tf.keras.models.load_model('sound_recognition_model.keras')
#     print("Model berhasil dimuat!")

#     # Pilih port
#     ports = list_ports()
#     if not ports:
#         return
        
#     port_idx = int(input("\nPilih nomor port: "))
#     port = ports[port_idx].device
    
#     print(f"Menggunakan port: {port}")
    
#     # Buka koneksi serial
#     ser = serial.Serial(port, 115200, timeout=1)
#     print("Koneksi serial dibuka")
    
#     try:
#         while True:
#             # Ambil data dari Serial
#             line = ser.readline().decode('utf-8').strip()
            
#             if line:  # Jika ada data
#                 try:
#                     # Split data menjadi array
#                     features = np.array([float(x) for x in line.split(',')])
                    
#                     # Pastikan panjang data sesuai
#                     if len(features) == 1002:  # 1000 audio + 2 fitur
#                         # Reshape untuk prediksi
#                         features = features.reshape(1, -1)
                        
#                         # Prediksi
#                         prediction = model.predict(features, verbose=0)[0]
                        
#                         # Tampilkan hasil
#                         print("\nHasil Prediksi:")
#                         print(f"Allahu Akbar: {prediction[0]*100:.1f}%")
#                         print(f"Subhanallah: {prediction[1]*100:.1f}%")
                        
#                         # Tentukan hasil
#                         if prediction[0] > prediction[1] and prediction[0] > 0.6:
#                             print("Terdeteksi: Allahu Akbar")
#                         elif prediction[1] > prediction[0] and prediction[1] > 0.6:
#                             print("Terdeteksi: Subhanallah")
#                         else:
#                             print("Tidak ada deteksi yang jelas")
                        
#                 except ValueError:
#                     # Jika data tidak bisa dikonversi ke float, abaikan
#                     continue
#                 except Exception as e:
#                     print(f"Error: {e}")
#                     continue
                    
#     except KeyboardInterrupt:
#         print("\nProgram dihentikan")
#     finally:
#         ser.close()
#         print("Port serial ditutup")

# if __name__ == "__main__":
#     main()


import serial
import numpy as np
import tensorflow as tf
import serial.tools.list_ports

def list_ports():
    """Menampilkan semua port serial yang tersedia"""
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("Tidak ada port serial ditemukan!")
        return None
        
    print("\nPort COM yang tersedia:")
    for i, p in enumerate(ports):
        print(f"{i}: {p.device} - {p.description}")
    return ports

def read_serial_data(ser):
    """Membaca data serial dengan penanganan error yang lebih baik"""
    try:
        # Baca data mentah
        raw_data = ser.readline()
        
        # Coba decode dengan berbagai encoding
        for encoding in ['utf-8', 'ascii', 'latin-1']:
            try:
                return raw_data.decode(encoding).strip()
            except UnicodeDecodeError:
                continue
                
        # Jika semua encoding gagal, gunakan decode errors='replace'
        return raw_data.decode('utf-8', errors='replace').strip()
    except Exception as e:
        print(f"Error membaca data serial: {e}")
        return None

def main():
    # Load model
    print("Loading model...")
    model = tf.keras.models.load_model('sound_recognition_model.keras')
    print("Model berhasil dimuat!")

    # Pilih port
    ports = list_ports()
    if not ports:
        return
        
    port_idx = int(input("\nPilih nomor port: "))
    port = ports[port_idx].device
    
    print(f"Menggunakan port: {port}")
    
    # Buka koneksi serial dengan timeout yang lebih pendek
    ser = serial.Serial(port, 115200, timeout=0.1)
    print("Koneksi serial dibuka")
    
    try:
        while True:
            # Baca data dengan fungsi yang telah diperbaiki
            line = read_serial_data(ser)
            
            if line:  # Jika ada data valid
                try:
                    # Hapus karakter non-printable
                    line = ''.join(char for char in line if char.isprintable())
                    
                    # Split data menjadi array
                    features = np.array([float(x) for x in line.split(',') if x.strip()])
                    
                    # Pastikan panjang data sesuai
                    if len(features) == 1002:  # 1000 audio + 2 fitur
                        # Reshape untuk prediksi
                        features = features.reshape(1, -1)
                        
                        # Prediksi
                        prediction = model.predict(features, verbose=0)[0]
                        
                        # Tampilkan hasil
                        print("\nHasil Prediksi:")
                        print(f"Allahu Akbar: {prediction[0]*100:.1f}%")
                        print(f"Subhanallah: {prediction[1]*100:.1f}%")
                        
                        # Tentukan hasil
                        if prediction[0] > prediction[1] and prediction[0] > 0.6:
                            print("Terdeteksi: Allahu Akbar")
                        elif prediction[1] > prediction[0] and prediction[1] > 0.6:
                            print("Terdeteksi: Subhanallah")
                        else:
                            print("Tidak ada deteksi yang jelas")
                    else:
                        print(f"Panjang data tidak sesuai: {len(features)}")
                        
                except ValueError as ve:
                    # Jika data tidak bisa dikonversi ke float
                    print(f"Error konversi data: {ve}")
                    continue
                except Exception as e:
                    print(f"Error pemrosesan: {e}")
                    continue
                    
    except KeyboardInterrupt:
        print("\nProgram dihentikan")
    except Exception as e:
        print(f"Error tidak terduga: {e}")
    finally:
        ser.close()
        print("Port serial ditutup")

if __name__ == "__main__":
    main()