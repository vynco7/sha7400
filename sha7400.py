# sha256_super_manual_1000params_82K_x7400.py
import struct
import time

# -------------------------
# ROTR / SHR
# -------------------------
def rotr(x,n):
    return ((x >> n) | (x << (32-n))) & 0xFFFFFFFF

def shr(x,n):
    return (x >> n) & 0xFFFFFFFF

# -------------------------
# Super functions (1000-input)
# -------------------------
def ch_super(inputs):
    result = 0
    for bit in range(32):
        ones = sum((x >> bit) & 1 for x in inputs)
        if ones > (len(inputs) // 2):
            result |= (1 << bit)
    return result & 0xFFFFFFFF

def maj_super(inputs):
    result = 0
    for bit in range(32):
        ones = sum((x >> bit) & 1 for x in inputs)
        if ones > (len(inputs) // 2):
            result |= (1 << bit)
    return result & 0xFFFFFFFF

def big_sigma0_super(inputs):
    r = rotr(inputs[0], 2)
    for x in inputs[1:]:
        r ^= rotr(x, 13)
    r ^= rotr(inputs[-1], 22)
    return r & 0xFFFFFFFF

def big_sigma1_super(inputs):
    r = rotr(inputs[0], 6)
    for x in inputs[1:]:
        r ^= rotr(x, 11)
    r ^= rotr(inputs[-1], 25)
    return r & 0xFFFFFFFF

def small_sigma0_super(inputs):
    r = rotr(inputs[0], 7)
    for x in inputs[1:]:
        r ^= rotr(x, 18)
    r ^= shr(inputs[-1], 3)
    return r & 0xFFFFFFFF

def small_sigma1_super(inputs):
    r = rotr(inputs[0], 17)
    for x in inputs[1:]:
        r ^= rotr(x, 19)
    r ^= shr(inputs[-1], 10)
    return r & 0xFFFFFFFF

# -------------------------
# 82 konstanta literal K
# -------------------------
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    0xca273ece, 0xd186b8c7, 0xeada7dd6, 0xf57d4f7f,
    0x06f067aa, 0x0a637dc5, 0x113f9804, 0x1b710b35,
    0x28db77f5, 0x32caab7b, 0x3c9ebe0a, 0x431d67c4,
    0x4cc5d4be, 0x597f299c, 0x5fcb6fab, 0x6c44198c,
    0x7f6a0dbb, 0x81c2c92e
]

H0 = [
    0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
]

# -------------------------
# Padding pesan
# -------------------------
def pad(msg):
    ml = len(msg)*8
    msg += b'\x80'
    while (len(msg)*8 + 64) % 512 != 0:
        msg += b'\x00'
    msg += struct.pack('>Q', ml)
    return msg

# -------------------------
# SHA-256 super manual (satu pesan)
# -------------------------
def sha256_super_manual(msg, params_1000):
    H = H0.copy()
    msg = pad(msg)
    for chunk_offset in range(0,len(msg),64):
        chunk = msg[chunk_offset:chunk_offset+64]
        W = list(struct.unpack('>16L', chunk)) + [0]*48
        for i in range(16,64):
            slice32 = params_1000[i%1000:i%1000+32]
            # Make sure slice32 has 32 items (wrap if needed)
            if len(slice32) < 32:
                slice32 = (slice32 * ((32 // len(slice32)) + 1))[:32]
            W[i] = (small_sigma1_super(slice32)+W[i-7]+small_sigma0_super(slice32)+W[i-16])&0xFFFFFFFF
        a,b,c,d,e,f,g,h = H
        for i in range(64):
            slice1000 = params_1000[i%1000:i%1000+1000] if len(params_1000)>=1000 else (params_1000*2)[:1000]
            k_i = K[i % len(K)]  # gunakan 82 konstanta
            T1 = (h + big_sigma1_super(slice1000) + ch_super(slice1000) + k_i + W[i]) & 0xFFFFFFFF
            T2 = (big_sigma0_super(slice1000) + maj_super(slice1000)) & 0xFFFFFFFF
            h=g; g=f; f=e; e=(d+T1)&0xFFFFFFFF; d=c; c=b; b=a; a=(T1+T2)&0xFFFFFFFF
        H = [(x+y)&0xFFFFFFFF for x,y in zip(H,[a,b,c,d,e,f,g,h])]
    return b''.join(struct.pack('>I',h) for h in H)

# -------------------------
# XOF-like generator -> output 7400 bits (925 bytes)
# -------------------------
def sha_super7400(msg, params_1000):
    OUT_BITS = 7400
    OUT_BYTES = OUT_BITS // 8  # 925
    out = bytearray()
    counter = 0
    # loop sampai cukup bytes
    while len(out) < OUT_BYTES:
        # domain-separate each chunk with counter
        chunk_msg = msg + b"::CNT::" + struct.pack(">I", counter)
        digest = sha256_super_manual(chunk_msg, params_1000)  # returns 32 bytes
        out.extend(digest)
        counter += 1
        # safety: avoid infinite loop, but practically won't happen
        if counter > 10000:
            break
    # trim to exact length
    out = bytes(out[:OUT_BYTES])
    return out

# -------------------------
# Contoh pemakaian
# -------------------------
if __name__=="__main__":
    # contoh params1000: kamu bisa ganti jadi list literal strings/numbers
    params1000 = [i for i in range(1000)]
    s = input("silahkan masukkann kode yang mau di enkripsi : ")
    msg = s.encode("utf-8")
    
    t0 = time.time()
    long_hash = sha_super7400(msg, params1000)
    elapsed = time.time() - t0

    print("SHA-super-7400 (hex, first 7400 chars):", long_hash.hex()[:7400])
    print("Total hex length:", len(long_hash.hex()))
    print("Panjang hash (bytes):", len(long_hash))
    print("Panjang hash (bits):", len(long_hash)*8)
    print("Elapsed: %.3fs" % elapsed)
