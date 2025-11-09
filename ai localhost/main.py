import tkinter as tk
from tkinter import messagebox
import os
import shutil
import zipfile
import requests

def show_message(msg):
    messagebox.showinfo("Pesan", msg)

# fungsi mengunduh file zip dari url anda

def dwonload_zip(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
        return False
# fungsi untuk mengekstrak file zip ke folder
def extract_zip(zip_path, extract_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        return True
    except zipfile.BadZipFile:
        print("Error: Invalid zip file")
        return False
    except Exception as e:
        print(f"Error extracting file: {e}")
        return False
# fungsi untuk menyalin file dari folder sumber ke folder tujuan
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        return True
    except Exception as e:
        print(f"Error copying file: {e}")
        return False
def copy_files_from_folder(source_folder, destination_folder):
    try:
        for file in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.copy(source_path, destination_path)
        return True
    except Exception as e:
        print(f"Error copying files: {e}")
        return False
def main ():
    # Menampilkan jendela file
    root = tk.Tk()
    root.title("ZIP Downloader")
    root.geometry("800x600")
    root.resizable(False, False)
    
    # Menampilkan label dan entry untuk URL
    label_url = tk.Label(root, text="URL File Zip:")
    entry_url = tk.Entry(root)
    label_url.grid(row=0, column=0, padx=10, pady=10)
    entry_url.grid(row=0, column=1, padx=10, pady=10)
    
    # Menampilkan button untuk mengunduh file zip
    # Menampilkan button untuk mengunduh file zip
    def handle_download():
        url = entry_url.get()
        save_path = entry_destination.get()
        if not url or not save_path:
            show_message("URL dan Folder Tujuan harus diisi!")
            return
        result = dwonload_zip(url, save_path)
        if result:
            show_message("Unduhan berhasil!")
        else:
            show_message("Unduhan gagal!")

    button_download = tk.Button(root, text="Unduh", command=handle_download)
    button_download.grid(row=1, column=0, padx=10, pady=10)

    # Menampilkan label untuk folder tujuan
    label_destination = tk.Label(root, text="Folder Tujuan:")
    entry_destination = tk.Entry(root)
    label_destination.grid(row=2, column=0, padx=10, pady=10)
    def handle_copy():
        source = entry_source.get()
        destination = entry_destination.get()
        if not source or not destination:
            show_message("Folder sumber dan tujuan harus diisi!")
            return
        result = copy_files_from_folder(source, destination)
        if result:
            show_message("Penyalinan berhasil!")
        else:
            show_message("Penyalinan gagal!")

    def handle_extract():
        zip_path = entry_destination.get()
        extract_path = entry_source.get()
        if not zip_path or not extract_path:
            show_message("Path file zip dan folder tujuan ekstrak harus diisi!")
            return
        result = extract_zip(zip_path, extract_path)
        if result:
            show_message("Ekstraksi berhasil!")
        else:
            show_message("Ekstraksi gagal!")

    button_extract = tk.Button(root, text="Ekstrak", command=handle_extract)
    button_extract.grid(row=3, column=0, padx=10, pady=10)
    # Menampilkan label untuk folder sumber
    label_source = tk.Label(root, text="Folder Sumber:")
    entry_source = tk.Entry(root)
    label_source.grid(row=4, column=0, padx=10, pady=10)
    entry_source.grid(row=4, column=1, padx=10, pady=10)
    
    # Menampilkan button untuk menyalin file dari folder sumber ke folder tujuan
    button_copy = tk.Button(root, text="Salin", command=handle_copy)
    button_copy.grid(row=5, column=0, padx=10, pady=10)
    
    # Menampilkan label untuk menampilkan pesan
    label_message = tk.Label(root, text="Pesan:")
    label_message.grid(row=6, column=0, padx=10, pady=10)
    
    # Menampilkan entry untuk menampilkan pesan
    entry_message = tk.Entry(root)
    entry_message.grid(row=6, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
