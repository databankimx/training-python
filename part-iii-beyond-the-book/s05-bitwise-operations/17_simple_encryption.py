"""Using XOR for Encryption and Decryption"""

def encrypt_decrypt(text: str, key: int) -> str:
    """Encrypts and decrypts a string using XOR"""
    return "".join([chr(ord(c) ^ key) for c in text])

def main() -> None:
    """Main program"""
    key = 30

    text = "Hello World!"
    print(f"Plain Text:     {text}")

    ciphertext = encrypt_decrypt(text, key)
    print(f"Encrypted Text: {ciphertext}")

    plaintext = encrypt_decrypt(ciphertext, key)
    print(f"Decrypted Text: {plaintext}")

if __name__ == "__main__":
    main()
