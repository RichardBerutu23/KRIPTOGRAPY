import itertools
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

# === FUNGSI PERMUTASI ===
def permutasi_menyeluruh(data):
    return list(itertools.permutations(data))

def permutasi_sebagian(data, k):
    return list(itertools.permutations(data, k))

def permutasi_keliling(data):
    if len(data) <= 1:
        return [data]
    pertama = data[0]
    hasil = []
    for perm in itertools.permutations(data[1:]):
        hasil.append([pertama] + list(perm))
    return hasil

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil


# === FUNGSI UNTUK TAMPILAN DAN EKSEKUSI ===
def tampilkan_hasil(judul, hasil):
    output_box.delete('1.0', tk.END)
    output_box.insert(tk.END, f"=== {judul} ===\n")
    output_box.insert(tk.END, f"Jumlah hasil: {len(hasil)}\n\n")
    for h in hasil:
        output_box.insert(tk.END, str(h) + "\n")
    output_box.insert(tk.END, "\n")

def konfirmasi_lanjut():
    jawab = messagebox.askyesno("Konfirmasi", "Apakah Anda ingin melanjutkan program?")
    if not jawab:
        root.destroy()

def jalankan_permutasi_menyeluruh():
    data = simpledialog.askstring("Input Data", "Masukkan elemen (pisahkan dengan spasi):").split()
    hasil = permutasi_menyeluruh(data)
    tampilkan_hasil("Permutasi Menyeluruh", hasil)
    konfirmasi_lanjut()

def jalankan_permutasi_sebagian():
    data = simpledialog.askstring("Input Data", "Masukkan elemen (pisahkan dengan spasi):").split()
    k = simpledialog.askinteger("Input K", "Masukkan jumlah elemen yang diambil (k):")
    hasil = permutasi_sebagian(data, k)
    tampilkan_hasil("Permutasi Sebagian", hasil)
    konfirmasi_lanjut()

def jalankan_permutasi_keliling():
    data = simpledialog.askstring("Input Data", "Masukkan elemen (pisahkan dengan spasi):").split()
    hasil = permutasi_keliling(data)
    tampilkan_hasil("Permutasi Keliling", hasil)
    konfirmasi_lanjut()

def jalankan_permutasi_berkelompok():
    jml_grup = simpledialog.askinteger("Input Jumlah Grup", "Masukkan jumlah grup:")
    grup = []
    for i in range(jml_grup):
        anggota = simpledialog.askstring("Input Grup", f"Masukkan anggota grup {i+1} (pisahkan dengan spasi):").split()
        grup.append(anggota)
    hasil = permutasi_berkelompok(grup)
    tampilkan_hasil("Permutasi Berkelompok", hasil)
    konfirmasi_lanjut()


# === GUI UTAMA ===
root = tk.Tk()
root.title("Program Permutasi GUI - Praktikum 3")
root.geometry("600x500")
root.resizable(False, False)

tk.Label(root, text="Pilih Jenis Permutasi", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Permutasi Menyeluruh", width=25, command=jalankan_permutasi_menyeluruh).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Permutasi Sebagian", width=25, command=jalankan_permutasi_sebagian).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Permutasi Keliling", width=25, command=jalankan_permutasi_keliling).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Permutasi Berkelompok", width=25, command=jalankan_permutasi_berkelompok).grid(row=1, column=1, padx=5, pady=5)


# Output box
output_box = scrolledtext.ScrolledText(root, width=70, height=15)
output_box.pack(padx=10, pady=10)

tk.Button(root, text="Keluar", command=root.destroy, bg="red", fg="white").pack(pady=5)

root.mainloop()
