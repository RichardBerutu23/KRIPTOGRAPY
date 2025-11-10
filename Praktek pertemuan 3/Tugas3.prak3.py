import itertools
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

# === Fungsi Faktorial dan Kombinasi ===
def faktorial(x):
    """Menghitung faktorial dari x"""
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

def kombinasi(n, r):
    """Menghitung nilai kombinasi C(n, r)"""
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# === Fungsi untuk Menampilkan Hasil ===
def tampilkan_hasil(judul, hasil_text):
    output_box.delete('1.0', tk.END)
    output_box.insert(tk.END, f"{judul}\n\n{hasil_text}")

def konfirmasi_lanjut():
    jawab = messagebox.askyesno("Konfirmasi", "Apakah Anda ingin melanjutkan program?")
    if not jawab:
        root.destroy()

# === Fungsi Utama Kombinasi ===
def jalankan_kombinasi():
    n = simpledialog.askinteger("Input N", "Masukkan jumlah total objek (n):")
    if n is None:
        return
    r = simpledialog.askinteger("Input R", "Masukkan jumlah objek yang dipilih (r):")
    if r is None:
        return

    if r > n or n <= 0 or r <= 0:
        messagebox.showerror("Error", "Nilai n dan r tidak valid (harus n ≥ r dan keduanya > 0).")
        return

    # Hitung nilai kombinasi
    jumlah = kombinasi(n, r)
    huruf = [chr(65 + i) for i in range(n)]
    hasil_kombinasi = list(itertools.combinations(huruf, r))

    # Siapkan teks hasil
    hasil_text = f"Jumlah kombinasi C({n}, {r}) = {jumlah}\n\nDaftar kombinasi (berdasarkan inisial huruf):\n"
    for idx, komb in enumerate(hasil_kombinasi, start=1):
        hasil_text += f"{idx}. {komb}\n"
    hasil_text += f"\nTotal kombinasi yang dihasilkan: {len(hasil_kombinasi)}"

    # Tampilkan di output box
    tampilkan_hasil("=== HASIL KOMBINASI ===", hasil_text)

    # Tampilkan konfirmasi
    konfirmasi_lanjut()

# === GUI TKINTER ===
root = tk.Tk()
root.title("Program Kombinasi GUI - Praktikum 3")
root.geometry("600x500")
root.resizable(False, False)

# Judul
tk.Label(root, text="PROGRAM KOMBINASI", font=("Arial", 16, "bold")).pack(pady=10)

# Tombol utama
tk.Button(root, text="Hitung Kombinasi", width=25, height=2, bg="#4CAF50", fg="white",
          command=jalankan_kombinasi).pack(pady=10)

# Kotak output
output_box = scrolledtext.ScrolledText(root, width=70, height=20)
output_box.pack(padx=10, pady=10)

# Tombol keluar
tk.Button(root, text="Keluar", bg="red", fg="white", width=10, command=root.destroy).pack(pady=5)

root.mainloop()
