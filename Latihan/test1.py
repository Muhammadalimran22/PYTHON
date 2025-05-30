import speech_recognition as sr
from collections import Counter
import difflib
import json
import os
from datetime import datetime
import threading
import time

class DzikirCounter:
    def __init__(self):
        self.known_words = {
            "subhanallah": ["subhanallah", "subahanallah", "subhanalloh", "subhanalloh", "subhanalah"],
            "alhamdulillah": ["alhamdulillah", "alhamdullilah", "alhamdulilah", "alhamdulilahi", "alhamdulilahi"],
            "allahuakbar": ["allahuakbar", "allahu akbar", "allahuekbar", "allahu ekbar", "allahuakbar"]
        }
        
        # Counter untuk dzikir
        self.counts = {
            "subhanallah": 0,
            "alhamdulillah": 0,
            "allahuakbar": 0
        }
        
        self.recognizer = sr.Recognizer()
        self.is_running = True
        
        # Pengaturan recognizer yang dioptimalkan
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.energy_threshold = 300
        self.recognizer.pause_threshold = 0.5
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.3

    def display_counts(self):
        """Thread untuk menampilkan hitungan secara real-time"""
        while self.is_running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n=== Hitungan Dzikir ===")
            print(f"Subhanallah  : {self.counts['subhanallah']}")
            print(f"Alhamdulillah: {self.counts['alhamdulillah']}")
            print(f"Allahu Akbar : {self.counts['allahuakbar']}")
            print("\nTekan Ctrl+C untuk keluar")
            time.sleep(0.5)

    def string_similarity(self, str1, str2):
        return difflib.SequenceMatcher(None, str1, str2).ratio()

    def process_audio(self, audio):
        try:
            # Mencoba Google Speech Recognition dengan bahasa Arab dan Indonesia
            try:
                text = self.recognizer.recognize_google(audio, language='ar-AR')
            except:
                text = self.recognizer.recognize_google(audio, language='id-ID')
            
            text = text.lower()
            
            # Cek setiap kata dzikir
            for dzikir_type, variations in self.known_words.items():
                # Jika ada kecocokan dengan salah satu variasi
                if any(self.string_similarity(text, var) > 0.7 for var in variations):
                    self.counts[dzikir_type] += 1
                    # Simpan ke file (opsional)
                    self.save_count(dzikir_type, text)
                    break
                    
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Gagal terhubung ke layanan Google Speech Recognition")
        except Exception as e:
            print(f"Error: {str(e)}")

    def save_count(self, dzikir_type, original_text):
        """Simpan hitungan ke file"""
        filename = "dzikir_log.json"
        entry = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'dzikir': dzikir_type,
            'original_text': original_text,
            'count': self.counts[dzikir_type]
        }
        
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    data = json.load(f)
            else:
                data = []
                
            data.append(entry)
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving to file: {str(e)}")

    def run(self):
        """Fungsi utama"""
        print("Memulai penghitung dzikir...")
        
        # Mulai thread untuk menampilkan hitungan
        display_thread = threading.Thread(target=self.display_counts)
        display_thread.daemon = True
        display_thread.start()
        
        with sr.Microphone() as source:
            print("Menyesuaikan dengan noise lingkungan...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                while self.is_running:
                    try:
                        audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=2)
                        self.process_audio(audio)
                    except sr.WaitTimeoutError:
                        continue
                        
            except KeyboardInterrupt:
                print("\nMenghentikan program...")
                self.is_running = False
                display_thread.join()
                print("\nProgram dihentikan")

if __name__ == "__main__":
    counter = DzikirCounter()
    counter.run()