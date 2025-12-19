# ----------------------------------
# Fungsi Perpangkatan Modular
# ----------------------------------
def mod_exp(base, exp, mod):
    hasil = 1
    proses = []

    while exp > 0:
        if exp % 2 == 1:
            hasil = (hasil * base) % mod
            proses.append(f"hasil = (hasil × {base}) mod {mod} = {hasil}")
        base = (base * base) % mod
        proses.append(f"base = base² mod {mod} = {base}")
        exp //= 2

    return hasil, proses


# ----------------------------------
# INPUT PARAMETER
# ----------------------------------
print("=== INPUT PARAMETER ELGAMAL ===")
p = int(input("Masukkan nilai p (prima): "))
g = int(input("Masukkan nilai g (generator): "))
x = int(input("Masukkan nilai x (kunci privat): "))
k = int(input("Masukkan nilai k (bilangan acak): "))

plaintext = input("Masukkan plaintext (maks 12 karakter): ")

if len(plaintext) > 50:
    print("❌ Plaintext terlalu panjang!")
    exit()

# ----------------------------------
# PEMBANGKITAN KUNCI PUBLIK
# ----------------------------------
print("\n=== PEMBANGKITAN KUNCI PUBLIK ===")
y, proses_y = mod_exp(g, x, p)
print(f"y = g^x mod p = {g}^{x} mod {p}")
for p1 in proses_y:
    print(" ", p1)
print("Kunci publik y =", y)

# ----------------------------------
# ENKRIPSI
# ----------------------------------
print("\n=== PROSES ENKRIPSI ===")
ciphertext = []

a, _ = mod_exp(g, k, p)  # a sama untuk semua karakter
yk, _ = mod_exp(y, k, p)

print(f"a = g^k mod p = {a}")
print(f"y^k mod p = {yk}")

for i, ch in enumerate(plaintext):
    m = ord(ch)
    b = (m * yk) % p
    ciphertext.append((a, b))

    print(f"\nKarakter ke-{i+1}: '{ch}'")
    print(f"ASCII m = {m}")
    print(f"b = m × y^k mod p = {m} × {yk} mod {p} = {b}")
    print(f"Ciphertext (a, b) = ({a}, {b})")

# ----------------------------------
# DEKRIPSI
# ----------------------------------
print("\n=== PROSES DEKRIPSI ===")
hasil_plaintext = ""

s, _ = mod_exp(a, x, p)
s_inv = pow(s, -1, p)

print(f"s = a^x mod p = {s}")
print(f"s⁻¹ = invers mod p = {s_inv}")

for i, (a, b) in enumerate(ciphertext):
    m = (b * s_inv) % p
    ch = chr(m)
    hasil_plaintext += ch

    print(f"\nCiphertext ke-{i+1}: (a={a}, b={b})")
    print(f"m = b × s⁻¹ mod p = {b} × {s_inv} mod {p} = {m}")
    print(f"Karakter = '{ch}'")

# ----------------------------------
# HASIL AKHIR
# ----------------------------------
print("\n=== HASIL AKHIR ===")
print("Plaintext asli   :", plaintext)
print("Plaintext hasil  :", hasil_plaintext)
