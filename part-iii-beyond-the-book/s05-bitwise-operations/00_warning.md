## Warning!

Just a heads-up...

For those of you who are mainly interested in practical programming, the early parts of this section may not be for you.

I'll be getting into the underlying theory of binary integers, the 
circuits used to add binary values, and the theoretical basis of the
integer system as implemented in the computer.

This is all valuable information and will help you understand why certain
situations in bitwise computation behave the way they do, but it's not
compulsory in order to perform the bitwise computations we'll learn later.

If you want to omit the theory and go straight to the logic and programming
with bitwise operations, skip to the [Truth Tables](./10_truth_tables.md)
lesson.

Here's how the lessons divide:

* Theory (lessons 01 to 09): integers, number bases, negative numbers, integer
  overflow, binary addition, and the ones' and twos' complement systems.
* Practical (lessons 10 to 19): truth tables, the bitwise AND, OR, NOT, and XOR
  operators, bit flags, bit shifts, and a simple encryption example.

Lessons 05 and 18 include small C programs that show overflow and underflow in a single
byte. They're there for comparison. Python integers don't overflow in that way,
so the same arithmetic gives a different result in Python.

Otherwise, hang on. It's a bit of a bumpy ride...

---
