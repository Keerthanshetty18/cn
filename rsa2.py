import math
def string_to_num(s):
    return int(''.join(f"{ord(c):03d}" for c in s))
def num_to_string(n):
    str_n = str(n)
    return ''.join(chr(int(str_n[i:i+3])) for i in range(0, len(str_n), 3))
p = int(input("Enter the p value: "))
q = int(input("Enter the q value: "))
n = p * q
print("n =", n)
phi = (p - 1) * (q - 1)
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1
print("e =", e)
k = 2
d = ((k * phi) + 1) // e  
print("d =", d)
print(f"Public key: ({e}, {n})")
print(f"Private key: ({d}, {n})")
msg = input("Enter the message: ")
msg_num = string_to_num(msg)
print(f"Numerical representation of the message: {msg_num}")
c = pow(msg_num, e, n)
print(f"Encrypted message: {c}")
M = pow(c, d, n)
decrypted_msg = num_to_string(M)
print(f"Decrypted message: {decrypted_msg}")