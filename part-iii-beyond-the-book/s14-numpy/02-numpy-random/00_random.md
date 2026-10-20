## The NumPy `random` Library

NumPy provides its own `random` library for generating and working with
random numbers. This is completely separate from the `random` module
delivered with the Python standard library.

It's worth reviewing a bit about "random" numbers to understand why this
module exists.

---

### What is a Random Number?

The term *random* does not mean that you will generate a different number
every time. Nor does it mean that there will not be sequences of 
repetition.

Instead, *random* means: not able to be logically predicted.

---

### Pseudo-Random Numbers

Because computers work with algorithms (repeatable series of 
instructions), it means that when a computer generates a so-called
"random" number, it is logically predictable (i.e.: given a fixed set of 
initial conditions, the computer will always generate the same number).

We refer to these numbers as *pseudo-random*, and much effort is made to
create difficult-to-predict initial conditions so as to overcome the
problem of the random number generator being determinate.

Modifying the initial conditions is referred to as *seeding* the random
number generator.

---

### Can We Generate Truly Random Numbers?

Short Answer: Yes

But, as you'd expect, it's more complicated than that.

In order to generate a truly random number on a computer we require 
random data from some external source, such as:

* Keystrokes
* Mouse Movements
* Data on the Network
* A [Wall of Lava Lamps](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)
* etc.

---

### Do We *Need* Truly Random Numbers?

Well, if you're responsible for the encryption that secures the global
Internet, yes.

In practice, however, appropriately seeded pseudo-random numbers are sufficient unless:

* The application is responsible for security and encryption
* The basis of the application requires randomness (a digital roulette
  wheel, e.g.)

All of the lessons in this section are using pseudo-random numbers.

---
