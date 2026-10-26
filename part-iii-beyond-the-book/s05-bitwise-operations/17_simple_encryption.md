## Bitwise XOR - Real-World Example: Encryption

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

One particularly interesting behavior of XOR is that it is reversible.

If you perform `z = x ^ y`, then `z ^ y` is equivalent to `x`

Imagine that we have some known value:  
$y=85_{10}=0101~0101_2$

Then we can take any value, for example  
$x=42_{10}=0010~1010_2$

and do the following:

> |||
> |-:|:-|
> |$0010~1010_2$|($x$)|
> |$\underline{\text{\^{}}~~~0101~0101_2}$|($y$)|
> |$0111~1111_2$||
> 
> |||
> |-:|:-|
> |$0111~1111_2$|($x~~\text{\^{}}~~y$)|
> |$\underline{\text{\^{}}~~~0101~0101_2}$|($y$)|
> |$0010~1010_2$|($x$)|

---

### Use-Case: Basic Encryption

This ability to XOR against a known value twice to obfuscate and then 
restore another value is the basis for a simple encryption/decryption 
algorithm.

Since the same key is used for both operations, this is called *symmetric 
key encryption*.

> Note: As presented here, this is **not** a secure algorithm and should 
> not be used for any production applications. This is just an example of a 
> simple procedure to encrypt and decrypt a piece of text.

---

### An Encryption/Decryption Algorithm

Because bitwise XOR is reversible, we can create a simple algorithm that
performs both the encryption and decryption process, requiring only a shared
key for performing the XOR.

Here, we'll just use an integer as the key. Then, we can step through each
character of the input string and perform an XOR of the character and the
key.

```python
def encrypt_decrypt(text: str, key: int) -> str:
    """Encrypts and decrypts a string using XOR"""
    return "".join([chr(ord(c) ^ key) for c in text])
```

Imagine that we use a key of 30 and pass in the string "Hello World!"

```python
# -- SNIP --

key = 30
text = "Hello World!"
cipherText = encrypt_decrypt(text, key)
print(f"Encrypted Text: {cipherText}")
```

Output:

```
Encrypted Text: V{rrq>Iqlrz?
```

---

#### Analysis

This yields a cipherText value of `V{rrq>Iqlrz?`

Let's step through the first character 'H' (ASCII $72_{10}$:
$0100~1000_2$)

> ||||
> |-:|-:|:-|
> |$0100~1000_2$|$72_{10}$|(H)|
> |$\underline{\text{\^{}}~~~0001~1110_2}$|$30_{10}$|(key)|
> |$0101~0110_2$|$86_{10}$|(V)|

ASCII $86$ is the 'V' character, which we see starting the cipherText

You can repeat this process with the ASCII values of the remaining 
characters to verify the value above.

---

Then, if we have the encrypted cipherText, we can pass it through the same
function (using the same key) to restore the original plaintext.

```python
# -- SNIP --

plainText = encrypt_decrypt(cipherText, key)
print(f"Decrypted Text: {plainText}")
```

Output:

```
Decrypted Text: Hello World!
```

---

#### Analysis

Let's look at the first character again...

'V' is $86_{10}$ ($0101~0110_2$)

> ||||
> |-:|-:|:-|
> |$0101~0110_2$|$86_{10}$|(V)|
> |$\underline{\text{\^{}}~~~0001~1110_2}$|$30_{10}$|(key)|
> |$0100~1000_2$|$72_{10}$|(H)|

Reversing the XOR operation restores the original plaintext character 'H'

Repeating that across the entire cipherText string returns the plainText
"Hello World!"

> Note: The `.py` prints a `Plain Text:` line before encrypting, so running the
> full script shows that line first:
>
> ```
> Plain Text:     Hello World!
> Encrypted Text: V{rrq>Iqlrz?
> Decrypted Text: Hello World!
> ```

---

### XOR Encryption Is Not Secure

As noted, this algorithm is not secure, for a number of reasons including:

* It uses a single integer value as its key. Since the characters here are
  single bytes, an attacker can brute-force the key by trying a small number of
  values (256 for single-byte characters).
* It requires both parties to share the same private key. Modern algorithms
  instead use a public key to encrypt and a private key to decrypt.

That said, the concept of using bitwise XOR with a symmetric key value is 
used widely as a step in some existing encryption algorithms like DES, 
AES, etc.

---

### High-Security Cryptography Does Not Use XOR as Its Core

Systems like RSA (that use *asymmetric key encryption*) are based on 
advanced number theory, and XOR isn't their core operation. Some RSA padding 
schemes (such as OAEP) do use XOR, but XOR can be (and is) used on its own in 
lower security applications where speed is the primary goal.

---

### But, XOR Encryption Does Have Some Up-Sides

Using bitwise XOR results in random ciphertext from non-random plaintext 
provided the key is a random value for each character being encrypted.

This means that when each character has its own random key, as in a one-time
pad, the ciphertext is immune to common cryptanalysis attacks like frequency
analysis. With one repeating key, the patterns in the plaintext can still show
through.

Importantly, single-byte XOR encryption is also very fast.

---

### How Can We Improve the Algorithm?

You can improve the security of this algorithm by:

* Using a one-time pad as a key, where each character is XORed against a 
  different key value from the pad.
* Using a larger (harder to guess) key
* Encrypting more than one byte at a time (or even varying the byte-length
  per operation)
* And many other techniques.

---

### A Little History

The NSA has called
[Vernam's Patent](https://patents.google.com/patent/US1310719A/en),
a circuit-based implementation of XOR, "perhaps one of the most important 
in the history of cryptography."

---
