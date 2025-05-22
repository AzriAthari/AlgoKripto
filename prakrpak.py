import math
from datetime import datetime

BASE_KEY = [9, 6, 5]

def get_day_offset():
    today = datetime.today()
    return (today.weekday() + 1) % 7 or 7

# Step 1: Shift + Reverse (base_key + day_offset )# mengubah ke ASCII-digeser-urutan dibalik
def apply_step1(text, day_offset):
    ascii_vals = [ord(c) for c in text]
    shifted = [(val + BASE_KEY[i % 3] + day_offset) % 256 for i, val in enumerate(ascii_vals)]
    reversed_shifted = shifted[::-1]
    print(f"Step 1: Shift + Reverse: {reversed_shifted}")
    return reversed_shifted

# Step 2: XOR posisi karakyer Genap/Ganjil berdasarkan day_offset
def apply_step2(data, day_offset):
    result = []
    for i, val in enumerate(data):
        key_val = BASE_KEY[i % 3]
        if day_offset % 2 == 0:
            if i % 2 == 0:
                result.append(val ^ ((key_val * day_offset) + 11))
            else:
                result.append(val)
        else:
            if i % 2 != 0:
                result.append(val ^ (key_val + day_offset))
            else:
                result.append(val)
    print(f"Step 2: XOR Genap/Ganjil: {result}")
    return result

# Step 3: Sinusoidal Mapping , 
def apply_step3(data, day_offset):
    result = []
    for i, val in enumerate(data):
        sine_val = int(127 * abs(math.sin(i + day_offset)))
        result.append((val + sine_val) % 256)
    print(f"Step 3: Sinusoidal Mapping: {result}")
    return result

# Step 4: Polynomial Modular Chaos
def apply_step4(data, day_offset):
    result = []
    for i, val in enumerate(data):
        poly = i**2 + 3*i + BASE_KEY[i % 3]
        transformed = (val * poly + day_offset) % 256
        result.append(transformed)
    print(f"Step 4: Polynomial Modular Chaos: {result}")
    return result

# Step 5: Modular Rotation (Index-based Key)  Nilai karakter digeser dengan nilai berdasarkan indeks karakter dan hari saat ini.
def apply_step5(data, day_offset):
    rotated = []
    for i, val in enumerate(data):
        key = (i * day_offset + BASE_KEY[i % 3]) % 256
        rotated.append((val + key) % 256)
    print(f"Step 5: Modular Rotation (Index-based Key): {rotated}")
    return rotated

def final_output(data):
    print(f"Final Encrypted Output: {data}")
    return data

# tahapa enkripsi
def encrypt(text):
    day_offset = get_day_offset()
    print(f"Day Offset: {day_offset}")
    
    step1 = apply_step1(text, day_offset)
    step2 = apply_step2(step1, day_offset)
    step3 = apply_step3(step2, day_offset)
    step4 = apply_step4(step3, day_offset)
    step5 = apply_step5(step4, day_offset)
    final_data = final_output(step5)
    
    return final_data, day_offset


def reverse_step5(data, day_offset):
    reversed_data = []
    for i, val in enumerate(data):
        key = (i * day_offset + BASE_KEY[i % 3]) % 256
        reversed_data.append((val - key) % 256)
    print(f"Step 5 (Reverse): Reverse Modular Rotation: {reversed_data}")
    return reversed_data

def reverse_step4(data, day_offset):
    result = []
    for i, val in enumerate(data):
        poly = i**2 + 3*i + BASE_KEY[i % 3]
        for x in range(256):
            if (x * poly + day_offset) % 256 == val:
                result.append(x)
                break
    print(f"Step 4 (Reverse): Reverse Polynomial Modular Chaos: {result}")
    return result

def reverse_step3(data, day_offset):
    result = []
    for i, val in enumerate(data):
        sine_val = int(127 * abs(math.sin(i + day_offset)))
        result.append((val - sine_val) % 256)
    print(f"Step 3 (Reverse): Reverse Sinusoidal Mapping: {result}")
    return result

def reverse_step2(data, day_offset):
    result = []
    for i, val in enumerate(data):
        key_val = BASE_KEY[i % 3]
        if day_offset % 2 == 0:
            if i % 2 == 0:
                result.append(val ^ ((key_val * day_offset) + 11))
            else:
                result.append(val)
        else:
            if i % 2 != 0:
                result.append(val ^ (key_val + day_offset))
            else:
                result.append(val)
    print(f"Step 2 (Reverse): Reverse XOR Genap/Ganjil: {result}")
    return result

def reverse_step1(data, day_offset):
    reversed_data = data[::-1]
    result = [(val - BASE_KEY[i % 3] - day_offset) % 256 for i, val in enumerate(reversed_data)]
    print(f"Step 1 (Reverse): Reverse Shift + Reverse: {result}")
    return result

def decrypt(encrypted_data, day_offset):
    step5 = reverse_step5(encrypted_data, day_offset)
    step4 = reverse_step4(step5, day_offset)
    step3 = reverse_step3(step4, day_offset)
    step2 = reverse_step2(step3, day_offset)
    step1 = reverse_step1(step2, day_offset)
    
    # Fix character ASCII range
    original_message = ''.join([chr(val % 128) for val in step1])
    return original_message

plaintext = input("Enter the message to encrypt: ")

encrypted_data, day_offset = encrypt(plaintext)
decrypted_message = decrypt(encrypted_data, day_offset)

print("\nEncrypted Data:")
print(f"Final Encrypted Output: {encrypted_data}")
print(f"Day Offset: {day_offset}")

print("\nDecrypted Message:")
print(f"Original Message: {decrypted_message}")
