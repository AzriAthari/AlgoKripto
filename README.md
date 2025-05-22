# 🔐 Custom Cryptography Project - Final Assignment

## 🧩 Overview
This project is a **custom-built symmetric encryption algorithm** designed for educational and experimental purposes. It encrypts text through **five mathematical and logical transformations**, using a fixed base key and dynamic elements like the day of encryption.

> 🗝️ **Base Key:** `[9, 6, 5]` — derived from birth date as an example.

## ✨ Features
- Day-based variation (messages differ based on day sent)
- Key cycling per character
- Multiple encryption stages with mathematical transformations
- Reversible decryption with accurate restoration
- Console-based encryption and decryption interface

---

## 🔐 Encryption Steps

### 🧮 Step 1: **Shift + Reverse**
- Convert text to ASCII.
- Add base key and `day_offset` (from day of the week).
- Reverse the order of characters.

### ⚡ Step 2: **XOR by Even/Odd Position**
- Based on whether the day is odd or even.
- Applies XOR to either even or odd character positions with derived values.

### 🌊 Step 3: **Sinusoidal Mapping**
- Apply a sine-based transformation:

- Adds dynamic, non-linear shifts based on character index and time.

### 📈 Step 4: **Polynomial Modular Chaos**
- Use a polynomial expression based on character position:

- Makes the encryption highly nonlinear and unique per character.

### 🧠 Step 5: **Bitwise Obfuscation**
- Applies a position-based left bit shift:
- Enhances entropy in final output.

---

## 🧪 Example
```bash
Input: Hai
Encrypted Output: [Encrypted byte list]
Decrypted Output: Hai
(today.weekday() + 1) % 7 or 7
