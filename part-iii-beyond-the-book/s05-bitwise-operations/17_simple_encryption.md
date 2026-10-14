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
> |$\underline{\^~~~0101~0101_2}$|($y$)|
> |$0111~1111_2$||
> 
> |||
> |-:|:-|
> |$0111~1111_2$|($xx~\^~~y$)|
> |$\underline{\^~~~0101~0101_2}$|($y$)|
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
    outString = []

    for i in range(len(text)):
        outString.append(chr(ord(text[i]) ^ key))
    
    return "".join(outString)
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
> |$\underline{\^~~~0001~1110_2}$|$30_{10}$|(key)|
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
> |$\underline{\^~~~0001~1110_2}$|$30_{10}$|(key)|
> |$0100~1000_2$|$72_{10}$|(H)|

Reversing the XOR operation restores the original plaintext character 'H'

Repeating that across the entire cipherText string returns the plainText
"Hello World!"

---

### XOR Encryption Is Not Secure

As noted, this algorithm is not secure, for a number of reasons including:

* It uses a single integer value as its key, which means that it is 
  possible to brute-force a decryption just by trying all of the possible 
  integer values.
* In our case, since we're performing XOR across single byte values, there
  can only be $256$ possible keys (or rather, for any larger key it 
  effectively behaves as `key = key % 256`, so any other part of the
  key can be ignored when guessing).
* It requires both parties to share the same private key (as opposed to
  more modern algorithms that use a public key to encrypt but individual
  private keys for decryption).

That said, the concept of using bitwise XOR with a symmetric key value is 
used widely as a step in some existing encryption algorithms like DES, 
AES,  tc.

---

### High-Security Cryptography Does Not Use XOR

Systems like RSA (that use *asymmetric key encryption*) are based on 
advanced number theory and do not use bitwise XOR, but XOR can be (and is) 
used in lower security applications where speed is the primary goal.

---

### But, XOR Encryption Does Have Some Up-Sides

Using bitwise XOR results in random ciphertext from non-random plaintext 
provided the key is a random value for each character being encrypted.

This means that even this simple mechanism can be made immune to common 
cryptanalysis attacks like frequency analysis.

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
