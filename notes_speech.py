import speech_recognition as sr
import sys
import os

# --- PENTING UNTUK WINDOWS ---
# Memastikan output console menggunakan UTF-8 agar tidak error saat print karakter khusus
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def main():
    # Inisialisasi Recognizer dan Mic
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # --- KONFIGURASI SENSITIVITAS ---
    # Matikan dynamic threshold agar tidak naik-turun sendiri
    recognizer.dynamic_energy_threshold = False 
    
    # Threshold: 300 (Ruangan sepi), 500-800 (Ruangan berisik)
    recognizer.energy_threshold = 300  
    
    # Waktu jeda diam sebelum dianggap selesai bicara
    recognizer.pause_threshold = 0.8 

    # Memberi sinyal ke aplikasi utama bahwa engine siap
    # Gunakan flush=True agar teks langsung dikirim tanpa ditahan di buffer
    print("DEBUG: Speech Engine Ready...", flush=True)

    # Loop utama (Listening Forever)
    # Proses ini akan terus berjalan sampai dimatikan (kill) oleh Macan Notes
    while True:
        try:
            with microphone as source:
                # Mendengarkan suara (Blocking mode)
                # Script akan berhenti di sini sampai ada suara masuk
                audio = recognizer.listen(source)

            try:
                # Mengubah suara menjadi teks (Google Speech Recognition)
                # Bahasa Indonesia (id-ID)
                text = recognizer.recognize_google(audio, language="id-ID")
                
                # --- PENGIRIMAN DATA KE APLIKASI UTAMA ---
                if text:
                    # Print teks bersih. QProcess di aplikasi utama akan menangkap ini.
                    print(text, flush=True)
                
            except sr.UnknownValueError:
                # Suara terdeteksi tapi tidak jelas kata-katanya
                # Kita diamkan saja (pass) atau kirim debug log
                # print("DEBUG: Suara tidak jelas", flush=True)
                pass
                
            except sr.RequestError:
                # Masalah koneksi internet atau API Google
                print("DEBUG: Koneksi Internet Bermasalah", flush=True)

        except KeyboardInterrupt:
            # Keluar loop jika ditekan Ctrl+C (saat testing manual)
            break
        except Exception as e:
            # Error tidak terduga lainnya
            print(f"DEBUG: Error {str(e)}", flush=True)

if __name__ == "__main__":
    main()