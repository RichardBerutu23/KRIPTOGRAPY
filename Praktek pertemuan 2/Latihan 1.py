# latihan1_repeat_calculator.py
# Program kalkulator yang berulang sampai user memilih berhenti (Y/T)

def kalkulasi(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return "Error: Pembagian dengan nol."
            return a / b
        elif op == '%':
            if b == 0:
                return "Error: Modulus dengan nol."
            return a % b
        elif op == '**':
            return a ** b
        else:
            return "Operator tidak dikenali."
    except Exception as e:
        return f"Terjadi error: {e}"

def main():
    print("=== Latihan 1: Kalkulator Berulang (Y/T) ===")
    while True:
        jawab = input("Apakah Anda ingin memulai operasi perhitungan? (Y/T): ").strip().lower()
        if jawab == 't':
            print("Program dihentikan. Terima kasih!")
            break
        elif jawab != 'y':
            print("Masukkan Y untuk ya atau T untuk tidak.")
            continue

        try:
            a = float(input("Masukkan nilai a: ").strip())
            b = float(input("Masukkan nilai b: ").strip())
        except ValueError:
            print("Input tidak valid. Masukkan angka (contoh: 3.5 atau 2).")
            continue

        op = input("Masukkan operator (+, -, *, /, %, **): ").strip()
        hasil = kalkulasi(a, b, op)
        print(f"Hasil: {a} {op} {b} = {hasil}\n")

if __name__ == "__main__":
    main()
