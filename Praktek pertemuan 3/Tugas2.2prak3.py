import tkinter as tk
from tkinter import messagebox, scrolledtext
import itertools

# Fungsi untuk menghasilkan semua kemungkinan penempatan
def generate_arrangements(n, r):
    book_names = [f"B{i+1}" for i in range(n)]
    for assignment in itertools.product(range(r), repeat=n):
        sections = [[] for _ in range(r)]
        for book_index, section_index in enumerate(assignment):
            sections[section_index].append(book_names[book_index])
        yield sections

# Fungsi untuk mencetak hasil ke area teks
def print_arrangements():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        if n < 0 or r < 1:
            messagebox.showwarning("Peringatan", "Pastikan n ≥ 0 dan r ≥ 1.")
            return
    except ValueError:
        messagebox.showwarning("Peringatan", "Masukkan angka valid untuk n dan r.")
        return

    total = pow(r, n)
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, f"Total kemungkinan penempatan: {total}\n\n")

    if total > 2000:
        jawab = messagebox.askyesno("Peringatan", f"Ada {total} kemungkinan. Ingin ditampilkan semua?")
        if not jawab:
            text_output.insert(tk.END, "❌ Dibatalkan menampilkan hasil besar.\n")
            return

    for idx, arrangement in enumerate(generate_arrangements(n, r), start=1):
        text_output.insert(tk.END, f"Case {idx}:\n")
        for sec_idx, books in enumerate(arrangement, start=1):
            isi = ', '.join(books) if books else "(kosong)"
            text_output.insert(tk.END, f"  Bagian {sec_idx}: {isi}\n")
        text_output.insert(tk.END, "-" * 30 + "\n")

    text_output.insert(tk.END, f"\nSelesai! Total {total} cara ditampilkan.\n")

# Fungsi untuk reset
def reset_fields():
    entry_n.delete(0, tk.END)
    entry_r.delete(0, tk.END)
    text_output.delete(1.0, tk.END)
    entry_n.focus()

# Fungsi keluar
def keluar():
    root.destroy()

# GUI utama
root = tk.Tk()
root.title("Program Penempatan Buku di Rak")
root.geometry("600x600")
root.config(bg="#f7f7f7")
root.resizable(False, False)

# Judul
label_judul = tk.Label(root, text="📚 Program Penempatan Buku di Rak", font=("Arial", 14, "bold"), bg="#f7f7f7", fg="#333")
label_judul.pack(pady=10)

# Frame input
frame_input = tk.Frame(root, bg="#f7f7f7")
frame_input.pack(pady=10)

# Input jumlah buku
label_n = tk.Label(frame_input, text="Jumlah Buku (n):", bg="#f7f7f7", font=("Arial", 11))
label_n.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_n = tk.Entry(frame_input, width=10, font=("Arial", 11))
entry_n.grid(row=0, column=1, pady=5)

# Input jumlah bagian
label_r = tk.Label(frame_input, text="Jumlah Bagian (r):", bg="#f7f7f7", font=("Arial", 11))
label_r.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_r = tk.Entry(frame_input, width=10, font=("Arial", 11))
entry_r.grid(row=1, column=1, pady=5)

# Frame tombol
frame_tombol = tk.Frame(root, bg="#f7f7f7")
frame_tombol.pack(pady=10)

btn_hitung = tk.Button(frame_tombol, text="Hitung & Tampilkan", command=print_arrangements,
                       bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=18)
btn_hitung.grid(row=0, column=0, padx=5)

btn_reset = tk.Button(frame_tombol, text="Reset", command=reset_fields,
                      bg="#f44336", fg="white", font=("Arial", 11, "bold"), width=10)
btn_reset.grid(row=0, column=1, padx=5)

btn_keluar = tk.Button(frame_tombol, text="Keluar", command=keluar,
                       bg="#9E9E9E", fg="white", font=("Arial", 11, "bold"), width=10)
btn_keluar.grid(row=0, column=2, padx=5)

# Output area
label_hasil = tk.Label(root, text="Hasil Penempatan:", font=("Arial", 11, "bold"), bg="#f7f7f7")
label_hasil.pack(pady=5)
text_output = scrolledtext.ScrolledText(root, width=70, height=22, font=("Consolas", 10), wrap=tk.WORD)
text_output.pack(pady=5)

# Fokus awal
entry_n.focus()

# Jalankan GUI
root.mainloop()
