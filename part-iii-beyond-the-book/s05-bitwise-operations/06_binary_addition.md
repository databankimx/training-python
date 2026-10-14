## Binary Addition

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

In order to understand how binary representations of integers work,
it's useful to first take a look at the way binary addition is handled
by a computer.

---

### The Binary Adder

A binary adder (at its core) is a circuit. Optimally, all that circuit 
should do is:

1. Take in two bits `A` & `B` (plus a carry bit `C`)
2. Add them together where  
   |A&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B|Sum|Carry|
   |:-:|:-:|:-:|
   |$0~+~0$|$0$|$0$|
   |$0~+~1$|$1$|$0$|
   |$1~+~0$|$1$|$0$|
   |$1~+~1$|$0$|$1$|
3. Return the output and pass the carry bit (if needed) to the next bit 
   adder

---

Such a circuit looks sort of like this:

```
      A & B are the input bits, and C is the carry
     ┌──────────────────────────────────────────────────────────────────────────────────┐
     │                          Full Adder                                              │
     │    ┌──────────────────┐              ┌──────────────────┐                        │
 A───│───>│             SUM  │───A ^ B──────│             SUM  │───(A ^ B) ^ C──────────│───> Sum
     │    │ Half Adder       │              │ Half Adder       │                        │
 B───│───>│            CARRY │───A & B──┐ ┌─│            CARRY │───C & (A ^ B)─┐        │
     │    └──────────────────┘          │ │ └──────────────────┘               │ ┌────┐ │
 Cin─│──────────────────────────────────│─┘                                    └─│    │ │
     │                                  │                                        │ ≥1 │─│───> Cout
     │                                  └────────────────────────────────────────│    │ │
     │                                                                           └────┘ │
     └──────────────────────────────────────────────────────────────────────────────────┘
```

---

### Addition with the Adder Circuit

Looking at the behavior of the circuit, we can see that there are eight 
possible scenarios to account for:

|A|B|Cin||Sum|Cout|
|:-:|:-:|:-:|:-:|:-:|:-:|
|$0$|$0$|$0$||$0$|$0$|
|$0$|$0$|$1$||$1$|$0$|
|$0$|$1$|$0$||$1$|$0$|
|$0$|$1$|$1$||$0$|$1$|
|$1$|$0$|$0$||$1$|$0$|
|$1$|$0$|$1$||$0$|$1$|
|$1$|$1$|$0$||$0$|$1$|
|$1$|$1$|$1$||$1$|$1$|

---

#### Case Study

Note: I am using the following symbols for bitwise operationd

|Symbol|Operation|
|:-:|:-:|
|$\&$|AND|
|$\|$|OR|
|$\sim$|NOT|
|$\oplus$|XOR|

Let's examine the case where $A = 1$, $B = 1$, and $C_{in} = 0$

This is equivalent to adding $1 + 1$ with no previous carry coming in.

* $A$ and $B$ enter the first half-adder
    * Both are $1$s, so:
        * SUM $(S_1)=A\oplus B=1\oplus1=0$
        * CARRY $(C_1)=A~\&~B=1~\&~1=1$
* $S_1$ and $C_{in}$ enter the second half-adder
    * Both are $0$s, so:
        * SUM $(S)=S_1\oplus C_{in}=0\oplus0=0$
        * CARRY $(C_2)=S_1~\&~C_{in}=0~\&~0=0$
* $S=0$, so the output sum is $0$
* $C_1+C_2=1+0=1$, and since $1\ge1$, $C_{out}=1$

So, binary $1+1=0$, with a carry (to the next place) of $1$

|||
|-:|-:|
|$01_2~~~$||
|$\underline{+~~01_2}~~~$|
|$10_2~~~$||
|$C\uparrow~\uparrow S$|

Hence, $1_2+1_2=10_2=2_{10}$

---

### Negatives in a Binary Adder

Looking at its minimal implementation, a circuit like this is not
designed to know the difference between positive and negative numbers.
All it does is add binary digits (and track the carry bit).

But, since there is no subtraction circuit, computers add negatives in
order to handle subtraction as an operation.

Because of that, we need a system of numbering in which the results from
the adder circuit are consistent for positive and negative numbers without 
requiring a different circuit for negative numbers (or subtraction).

We know that we can use a specific bit for the sign, but how do we create a
binary numbering system where the results are consistent?

The upcoming topics will explain that...

---
