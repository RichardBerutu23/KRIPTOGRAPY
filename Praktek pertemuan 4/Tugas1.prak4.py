import tkinter as tk
from tkinter import messagebox

# Fungsi substitusi cipher
def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk menjalankan enkripsi
def enkripsi():
    plaintext = entry_plaintext.get().upper()
    aturan_input = text_aturan.get("1.0", tk.END).strip()

    if not plaintext:
        messagebox.showwarning("Peringatan", "Masukkan plaintext terlebih dahulu!")
        return

    if not aturan_input:
        messagebox.showwarning("Peringatan", "Masukkan aturan substitusi terlebih dahulu!")
        return

    try:
        aturan = {}
        for line in aturan_input.splitlines():
            if ':' in line:
                key, value = line.split(':')
                aturan[key.strip().upper()] = value.strip().upper()

        ciphertext = substitusi_cipher(plaintext, aturan)
        label_hasil.config(text=f"Hasil Ciphertext: {ciphertext}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi reset
def reset():
    entry_plaintext.delete(0, tk.END)
    text_aturan.delete("1.0", tk.END)
    label_hasil.config(text="Hasil Ciphertext: ")
    entry_plaintext.focus()

# GUI utama
root = tk.Tk()
root.title("Program Substitusi Cipher")
root.geometry("470x420")
root.resizable(False, False)
root.configure(bg="#f7f7f7")

# Judul
label_judul = tk.Label(root, text="🔐 Program Substitusi Cipher", font=("Arial", 14, "bold"), bg="#f7f7f7")
label_judul.pack(pady=10)

# Input plaintext
label_plaintext = tk.Label(root, text="Masukkan Plaintext:", font=("Arial", 10), bg="#f7f7f7")
label_plaintext.pack()
entry_plaintext = tk.Entry(root, width=45, font=("Arial", 11))
entry_plaintext.pack(pady=5)

# Input aturan substitusi
label_aturan = tk.Label(root, text="Masukkan Aturan Substitusi (format: A:B)", font=("Arial", 10), bg="#f7f7f7")
label_aturan.pack()
text_aturan = tk.Text(root, width=45, height=8, font=("Consolas", 10))
text_aturan.pack(pady=5)

# Frame tombol
frame_tombol = tk.Frame(root, bg="#f7f7f7")
frame_tombol.pack(pady=10)

# Tombol Enkripsi
btn_enkripsi = tk.Button(frame_tombol, text="Enkripsi", command=enkripsi,
                         bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=12)
btn_enkripsi.grid(row=0, column=0, padx=5)

# Tombol Reset
btn_reset = tk.Button(frame_tombol, text="Ulang", command=reset,
                      bg="#f44336", fg="white", font=("Arial", 11, "bold"), width=12)
btn_reset.grid(row=0, column=1, padx=5)

# Label hasil
label_hasil = tk.Label(root, text="Hasil Ciphertext: ", font=("Arial", 12, "bold"), fg="blue", bg="#f7f7f7")
label_hasil.pack(pady=10)

# Jalankan GUI
root.mainloop()
