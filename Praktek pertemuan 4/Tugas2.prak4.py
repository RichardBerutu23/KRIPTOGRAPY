import tkinter as tk
from tkinter import messagebox, scrolledtext
import math

# ==============================
#  Fungsi Substitusi Cipher
# ==============================
def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

# ==============================
#  Fungsi Transposisi Cipher
# ==============================
def transposisi_cipher(text, kolom):
    text = text.replace(" ", "").upper()
    baris = math.ceil(len(text) / kolom)
    tabel = []
    index = 0

    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            if index < len(text):
                baris_data.append(text[index])
                index += 1
            else:
                baris_data.append("X")  # padding
        tabel.append(baris_data)

    # Buat hasil baca per kolom
    ciphertext = ""
    for j in range(kolom):
        for i in range(baris):
            ciphertext += tabel[i][j]

    return ciphertext, tabel

# ==============================
#  Fungsi tombol "Proses"
# ==============================
def proses_cipher():
    plaintext = entry_plaintext.get().upper()
    aturan_input = text_aturan.get("1.0", tk.END).strip()
    kolom_input = entry_kolom.get().strip()

    if not plaintext:
        messagebox.showwarning("Peringatan", "Masukkan plaintext terlebih dahulu!")
        return
    if not aturan_input:
        messagebox.showwarning("Peringatan", "Masukkan aturan substitusi terlebih dahulu!")
        return
    if not kolom_input.isdigit() or int(kolom_input) < 2:
        messagebox.showwarning("Peringatan", "Masukkan jumlah kolom (≥2)!")
        return

    kolom = int(kolom_input)

    # Buat dictionary aturan substitusi
    try:
        aturan = {}
        for line in aturan_input.splitlines():
            if ':' in line:
                key, value = line.split(':')
                aturan[key.strip().upper()] = value.strip().upper()
    except Exception as e:
        messagebox.showerror("Error", f"Aturan tidak valid: {e}")
        return

    # Proses substitusi
    hasil_substitusi = substitusi_cipher(plaintext, aturan)

    # Proses transposisi dari hasil substitusi
    hasil_transposisi, tabel_transposisi = transposisi_cipher(hasil_substitusi, kolom)

    # Format tabel kolom transposisi
    tabel_str = ""
    for row in tabel_transposisi:
        tabel_str += "  ".join(row) + "\n"

    # ==============================
    #  Format hasil sederhana
    # ==============================
    hasil_laporan = (
        f"Plaintext:\n{plaintext}\n\n"
        f"Hasil Substitusi Cipher:\n{hasil_substitusi}\n\n"
        f"Hasil Substitusi + Transposisi (tampilan kolom):\n\n"
        f"{tabel_str}\n"
        f"Ciphertext Akhir (dibaca per kolom):\n{hasil_transposisi}\n"
    )

    # Tampilkan hasil di area output
    text_hasil.delete(1.0, tk.END)
    text_hasil.insert(tk.END, hasil_laporan)

# ==============================
#  Fungsi tombol "Reset"
# ==============================
def reset_fields():
    entry_plaintext.delete(0, tk.END)
    text_aturan.delete("1.0", tk.END)
    entry_kolom.delete(0, tk.END)
    text_hasil.delete(1.0, tk.END)
    entry_plaintext.focus()

# ==============================
#  Fungsi tombol "Keluar"
# ==============================
def keluar():
    root.destroy()

# ==============================
#  GUI Utama
# ==============================
root = tk.Tk()
root.title("🔐 Substitusi + Transposisi Cipher (Versi Ringkas)")
root.geometry("680x700")
root.config(bg="#f7f7f7")
root.resizable(False, False)

# Judul
label_judul = tk.Label(root, text="🔐 Substitusi + Transposisi Cipher", 
                       font=("Arial", 14, "bold"), bg="#f7f7f7", fg="#333")
label_judul.pack(pady=10)

# Frame input plaintext
frame_plain = tk.Frame(root, bg="#f7f7f7")
frame_plain.pack(pady=5)
tk.Label(frame_plain, text="Masukkan Plaintext:", bg="#f7f7f7", font=("Arial", 10)).grid(row=0, column=0, sticky="w")
entry_plaintext = tk.Entry(frame_plain, width=60, font=("Arial", 11))
entry_plaintext.grid(row=1, column=0, pady=5)

# Frame aturan substitusi
frame_aturan = tk.Frame(root, bg="#f7f7f7")
frame_aturan.pack(pady=5)
tk.Label(frame_aturan, text="Masukkan Aturan Substitusi (format: A:B):", bg="#f7f7f7", font=("Arial", 10)).pack(anchor="w")
text_aturan = tk.Text(frame_aturan, width=60, height=6, font=("Consolas", 10))
text_aturan.pack(pady=5)

# Frame kolom transposisi
frame_kolom = tk.Frame(root, bg="#f7f7f7")
frame_kolom.pack(pady=5)
tk.Label(frame_kolom, text="Masukkan Jumlah Kolom (blok transposisi):", bg="#f7f7f7", font=("Arial", 10)).pack(anchor="w")
entry_kolom = tk.Entry(frame_kolom, width=10, font=("Arial", 11))
entry_kolom.pack(pady=5)

# Frame tombol
frame_tombol = tk.Frame(root, bg="#f7f7f7")
frame_tombol.pack(pady=10)
btn_proses = tk.Button(frame_tombol, text="Proses Cipher", command=proses_cipher,
                       bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=15)
btn_proses.grid(row=0, column=0, padx=5)

btn_reset = tk.Button(frame_tombol, text="Reset", command=reset_fields,
                      bg="#f44336", fg="white", font=("Arial", 11, "bold"), width=10)
btn_reset.grid(row=0, column=1, padx=5)

btn_keluar = tk.Button(frame_tombol, text="Keluar", command=keluar,
                       bg="#9E9E9E", fg="white", font=("Arial", 11, "bold"), width=10)
btn_keluar.grid(row=0, column=2, padx=5)

# Frame hasil
frame_hasil = tk.Frame(root, bg="#f7f7f7")
frame_hasil.pack(pady=10)
tk.Label(frame_hasil, text="Hasil Proses Cipher:", bg="#f7f7f7", font=("Arial", 11, "bold")).pack(anchor="w")
text_hasil = scrolledtext.ScrolledText(frame_hasil, width=80, height=20, font=("Consolas", 10))
text_hasil.pack(pady=5)

entry_plaintext.focus()
root.mainloop()
