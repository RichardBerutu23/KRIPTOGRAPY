# -----------------------------
# Program Enkripsi RSA Sederhana
# p = 17, q = 11, e = 7
# -----------------------------

# Fungsi untuk menghitung gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fungsi untuk menghitung inverse modulo
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# -----------------------------
# 1. Inisialisasi nilai p, q, e
# -----------------------------
p = 17
q = 11
e = 7

# -----------------------------
# 2. Hitung n dan phi(n)
# -----------------------------
n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("phi(n) =", phi)

# -----------------------------
# 3. Hitung kunci privat (d)
# -----------------------------
d = mod_inverse(e, phi)
print("Kunci Privat d =", d)

# -----------------------------
# 4. Fungsi enkripsi RSA
# -----------------------------
def encrypt(m, e, n):
    return pow(m, e, n)  # m^e mod n

# -----------------------------
# 5. Input plaintext manual
# -----------------------------
plaintext = int(input("Masukkan plaintext (bilangan): "))

# -----------------------------
# 6. Enkripsi RSA
# -----------------------------
ciphertext = encrypt(plaintext, e, n)

print("Plaintext =", plaintext)
print("Ciphertext =", ciphertext)
