## One's Complement

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

Another option that was looked at in early computer design was to implement
negative numbers as the ***one's complement*** of their positive 
counterparts.

One's complement is simply the binary complement (opposite value for each 
bit) of the positive value.

---

So with our known positive values (in our imaginary 4-bit integer):

* $0000_2=0_{10}$
* $0001_2=1_{10}$
* $0010_2=2_{10}$
* $0011_2=3_{10}$
* $0100_2=4_{10}$
* $0101_2=5_{10}$
* $0110_2=6_{10}$
* $0111_2=7_{10}$

---

The one's complement implementation would look like this:

* $1111_2=-0_{10}$
* $1110_2=-1_{10}$
* $1101_2=-2_{10}$
* $1100_2=-3_{10}$
* $1011_2=-4_{10}$
* $1010_2=-5_{10}$
* $1001_2=-6_{10}$
* $1000_2=-7_{10}$

---

### OK - So what's wrong with this one?

We still have the problem of both positive and negative zeroes.

Addition is also still a problem, though less so than in the previous example.

Let's look at the same examples we saw in the previous topic:

---

### $1-1$

> ||
> |-:|
> |$0001_2$|
> |$\underline{+~1110_2}$|
> |$1111_2$|

This gives a result of $1-1=-0$, which isn't perfect (because what
even is $-0$?), but at least it gibes with reality.

However, if we add 1 to the result:

> |||
> |-:|-|
> |$1111_2$||
> |$\underline{+~0001_2}$||
> |$1\Larr0000_2$|*lost (overflowed) carry bit here|

We end up with the original expected value of $0$

Hang onto this idea...

---

### $7-3$

> |||
> |-:|-|
> |$0111_2$||
> |$\underline{+~1100_2}$||
> |$1\Larr0011_2$|*lost (overflowed) carry bit here|

Which gives $7-3=3$, which is wrong, but again if we add $1$ (which
we can think of as wrapping the lost carry bit back around to the $1$s
place)...

> ||
> |-:|
> |$0011_2$|
> |$\underline{+~0001_2}$|
> |$0100_2$|

We get the right answer of $7-3=4$

Seem's like we might be onto something with this business of adding $1$
to the result of adding a one's complement negative number.

---

### So Close!

This business of wrapping the lost carry bit doesn't make sense without 
extra hardware (and extra memory, since we don't have a fifth bit to hold 
it in).

So, how do we address the problem of getting results that are off by one?
And is there a way to get rid of that pesky negative zero?

---
