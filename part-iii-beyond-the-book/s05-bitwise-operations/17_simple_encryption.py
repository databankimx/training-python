"""Using XOR for Encryption and Decryption"""

def encrypt_decrypt(text: str, key: int) -> str:
    """Encrypts and decrypts a string using XOR"""
    return "".join([chr(ord(c) ^ key) for c in text])

def main() -> None:
    """Main program"""
    key = 30

    text = "Hello World!"
    print(f"Plain Text:     {text}")

    cipherText = encrypt_decrypt(text, key)
    print(f"Encrypted Text: {cipherText}")

    plainText = encrypt_decrypt(cipherText, key)
    print(f"Decrypted Text: {plainText}")

if __name__ == "__main__":
    main()
