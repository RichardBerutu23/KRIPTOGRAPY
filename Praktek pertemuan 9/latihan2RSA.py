import random
import math
from typing import List, Tuple

# ---------------------------
# Util: Sieve untuk primes 50-200
# ---------------------------
def sieve_primes(low: int, high: int) -> List[int]:
    sieve = [True] * (high + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(high**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, high + 1, i):
                sieve[j] = False
    return [p for p in range(low, high + 1) if sieve[p]]

# ---------------------------
# Util: GCD
# ---------------------------
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# ---------------------------
# Extended Euclidean -> modular inverse
# returns (g, x, y) such that ax + by = g = gcd(a,b)
# ---------------------------
def extended_gcd(a: int, b: int) -> Tuple[int,int,int]:
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

def modinv(e: int, phi: int) -> int:
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        return None
    return x % phi

# ---------------------------
# Pilih p, q acak dari primes
# ---------------------------
def pick_random_pq(low=50, high=200) -> Tuple[int,int]:
    primes = sieve_primes(low, high)
    p = random.choice(primes)
    q = random.choice(primes)
    while q == p:
        q = random.choice(primes)
    return p, q

# ---------------------------
# Pilih e acak (1 < e < phi) dengan gcd(e,phi)=1
# ---------------------------
def pick_random_e(phi: int) -> int:
    # try random candidates until find coprime
    attempts = 0
    while True:
        attempts += 1
        e = random.randint(3, phi - 1)
        if gcd(e, phi) == 1:
            return e
        if attempts > 10000:
            raise RuntimeError("Gagal menemukan e coprime dengan phi setelah banyak percobaan")

# ---------------------------
# Helper: split bytes into blocks fitting into n
# ---------------------------
def bytes_to_blocks(b: bytes, block_size: int) -> List[int]:
    blocks = [int.from_bytes(b[i:i+block_size], byteorder='big')
              for i in range(0, len(b), block_size)]
    return blocks

def blocks_to_bytes(blocks: List[int], block_size: int) -> bytes:
    out = bytearray()
    for blk in blocks:
        out.extend(blk.to_bytes(block_size, byteorder='big'))
    # trim possible leading zero bytes from first block? keep exact original length handled externally
    return bytes(out)

# ---------------------------
# RSA encrypt/decrypt
# ---------------------------
def encrypt_block(m: int, e: int, n: int) -> int:
    return pow(m, e, n)

def decrypt_block(c: int, d: int, n: int) -> int:
    return pow(c, d, n)

# ---------------------------
# Program utama
# ---------------------------
def main():
    print("=== Program RSA (Latihan 2) ===")
    # 1. Pilih p, q acak
    p, q = pick_random_pq(50, 200)
    n = p * q
    phi = (p - 1) * (q - 1)

    print("\nLangkah 1: Pemilihan bilangan prima (acak)")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = p * q = {n}")
    print(f"phi(n) = (p-1)*(q-1) = {phi}")

    # 2. Pilih e
    e = pick_random_e(phi)
    print("\nLangkah 2: Memilih e (relatif prima dengan phi)")
    print(f"e = {e}  (cek gcd(e, phi) = {gcd(e, phi)})")

    # 3. Hitung d
    d = modinv(e, phi)
    if d is None:
        print("Tidak ditemukan invers modular untuk e (ini tidak harus terjadi).")
        return
    print("\nLangkah 3: Menghitung kunci privat d (invers modulo e mod phi)")
    print(f"d = {d}  (karena e * d ≡ 1 (mod phi))")

    print("\nKunci publik (e, n) =", (e, n))
    print("Kunci privat d =", d)

    # 4. Input plaintext
    raw = input("\nMasukkan plaintext (boleh teks atau angka) : ").rstrip("\n")
    # cek apakah input adalah bilangan bulat:
    is_number = False
    try:
        m_number = int(raw)
        is_number = True
    except ValueError:
        is_number = False

    if is_number:
        # pastikan 0 <= m < n
        if not (0 <= m_number < n):
            print("\nERROR: Plaintext numerik harus 0 <= m < n (nilai n = {}).".format(n))
            print("Silakan jalankan ulang dan masukkan angka lebih kecil dari n.")
            return

        print("\n--- Proses Enkripsi (angka) ---")
        print(f"Plaintext (m) = {m_number}")
        c = encrypt_block(m_number, e, n)
        print(f"Ciphertext (c = m^e mod n) = {c}")

        m_decrypted = decrypt_block(c, d, n)
        print(f"Setelah dekripsi (m' = c^d mod n) = {m_decrypted}")

        print("\nVerifikasi: ", "BERHASIL" if m_decrypted == m_number else "GAGAL")

    else:
        # Treat as text. Convert to bytes and split into blocks such that each block < n.
        b_plain = raw.encode('utf-8')
        # determine max block size in bytes: need 256^k <= n -> k = floor((bitlen(n)-1)/8)
        k_bytes = max(1, (n.bit_length() - 1) // 8)  # at least 1 byte
        print("\n--- Proses Enkripsi (teks) ---")
        print(f"Plaintext teks: '{raw}'")
        print(f"Plaintext (bytes): {b_plain}")
        print(f"Ukuran block (byte) yang digunakan = {k_bytes} (agar setiap blok < n)")

        # split into blocks
        blocks = bytes_to_blocks(b_plain, k_bytes)
        print(f"\nKonversi blok -> bilangan bulat (m_i), semua harus < n")
        for i, blk in enumerate(blocks):
            print(f"  Block {i}: integer = {blk}  (cek < n: {blk < n})")
            if blk >= n:
                print("\nERROR: Ada blok yang >= n — pilih p,q lebih besar atau kurangi panjang teks per blok.")
                return

        # encrypt each block
        ciphertext_blocks = []
        print("\nEnkripsi tiap blok (c_i = m_i^e mod n):")
        for i, mblk in enumerate(blocks):
            cblk = encrypt_block(mblk, e, n)
            ciphertext_blocks.append(cblk)
            print(f"  Block {i}: m={mblk} -> c={cblk}")

        # dekripsi tiap blok
        decrypted_blocks = []
        print("\nDekripsi tiap blok (m'_i = c_i^d mod n):")
        for i, cblk in enumerate(ciphertext_blocks):
            mblk = decrypt_block(cblk, d, n)
            decrypted_blocks.append(mblk)
            print(f"  Block {i}: c={cblk} -> m'={mblk}")

        # gabungkan kembali ke bytes
        # each decrypted block must be encoded back to exactly k_bytes (leading zeros preserved)
        recovered_bytes = bytearray()
        for mblk in decrypted_blocks:
            recovered_bytes.extend(mblk.to_bytes(k_bytes, byteorder='big'))

        # recovered_bytes may include padding zeros if original length not multiple of k_bytes
        # trim to original length
        recovered_bytes = bytes(recovered_bytes)[:len(b_plain)]
        try:
            recovered_text = recovered_bytes.decode('utf-8')
        except Exception as ex:
            recovered_text = None
            print("\nWarning: Gagal decode hasil dekripsi ke UTF-8:", ex)

        print("\nHasil gabungan bytes setelah dekripsi:", recovered_bytes)
        print("Hasil teks setelah dekripsi:", repr(recovered_text))
        print("\nVerifikasi teks sama dengan asli?:", "BERHASIL" if recovered_text == raw else "GAGAL")

    print("\n--- Selesai ---")

if __name__ == "__main__":
    main()
