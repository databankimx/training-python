## Bonus Lesson: Text Encoding

### Characters Must Be Encoded

A computer knows only two possible values: `0` and `1`.

Because of this, in order to compute and display human-readable text, there
must be a standardized way to encode text as a binary number.

<img src="./baudot-code.png" style="width: 200px">

As far back as the 1870s, Émile Baudot developed a five-bit code for telegraphy
(see above). It encoded the alphabet as patterns of on and off signals, which
were sent over a wire and punched onto paper tape. Different encoding standards
have been introduced over time since then.

---

### ASCII Encoding

Originally introduced in 1963 (and most recently updated in 1986), the
American Standard Code for Information Interchange (or **ASCII**) is still the
default encoding for many computer applications today.

ASCII encodes 128 characters as 7-bit binary values (as seen below):

<details>
<summary>ASCII Table</summary>

|  Dec |  Hex  | Char  |     |  Dec |  Hex  |  Char   |     |  Dec |  Hex  | Char  |     |   Dec |  Hex  | Char  |
| ---: | :---: | :---: | --- | ---: | :---: | :-----: | --- | ---: | :---: | :---: | --- | ----: | :---: | :---: |
|  `0` | `00`  | `NUL` |     | `32` | `20`  | `Space` |     | `64` | `40`  |  `@`  |     |  `96` | `60`  | `` ` ``  |
|  `1` | `01`  | `SOH` |     | `33` | `21`  |   `!`   |     | `65` | `41`  |  `A`  |     |  `97` | `61`  |  `a`  |
|  `2` | `02`  | `STX` |     | `34` | `22`  |   `"`   |     | `66` | `42`  |  `B`  |     |  `98` | `62`  |  `b`  |
|  `3` | `03`  | `ETX` |     | `35` | `23`  |   `#`   |     | `67` | `43`  |  `C`  |     |  `99` | `63`  |  `c`  |
|  `4` | `04`  | `EOT` |     | `36` | `24`  |   `$`   |     | `68` | `44`  |  `D`  |     | `100` | `64`  |  `d`  |
|  `5` | `05`  | `ENQ` |     | `37` | `25`  |   `%`   |     | `69` | `45`  |  `E`  |     | `101` | `65`  |  `e`  |
|  `6` | `06`  | `ACK` |     | `38` | `26`  |   `&`   |     | `70` | `46`  |  `F`  |     | `102` | `66`  |  `f`  |
|  `7` | `07`  | `BEL` |     | `39` | `27`  |   `'`   |     | `71` | `47`  |  `G`  |     | `103` | `67`  |  `g`  |
|  `8` | `08`  | `BS`  |     | `40` | `28`  |   `(`   |     | `72` | `48`  |  `H`  |     | `104` | `68`  |  `h`  |
|  `9` | `09`  | `HT`  |     | `41` | `29`  |   `)`   |     | `73` | `49`  |  `I`  |     | `105` | `69`  |  `i`  |
| `10` | `0A`  | `LF`  |     | `42` | `2A`  |   `*`   |     | `74` | `4A`  |  `J`  |     | `106` | `6A`  |  `j`  |
| `11` | `0B`  | `VT`  |     | `43` | `2B`  |   `+`   |     | `75` | `4B`  |  `K`  |     | `107` | `6B`  |  `k`  |
| `12` | `0C`  | `FF`  |     | `44` | `2C`  |   `,`   |     | `76` | `4C`  |  `L`  |     | `108` | `6C`  |  `l`  |
| `13` | `0D`  | `CR`  |     | `45` | `2D`  |   `-`   |     | `77` | `4D`  |  `M`  |     | `109` | `6D`  |  `m`  |
| `14` | `0E`  | `SO`  |     | `46` | `2E`  |   `.`   |     | `78` | `4E`  |  `N`  |     | `110` | `6E`  |  `n`  |
| `15` | `0F`  | `SI`  |     | `47` | `2F`  |   `/`   |     | `79` | `4F`  |  `O`  |     | `111` | `6F`  |  `o`  |
| `16` | `10`  | `DLE` |     | `48` | `30`  |   `0`   |     | `80` | `50`  |  `P`  |     | `112` | `70`  |  `p`  |
| `17` | `11`  | `DC1` |     | `49` | `31`  |   `1`   |     | `81` | `51`  |  `Q`  |     | `113` | `71`  |  `q`  |
| `18` | `12`  | `DC2` |     | `50` | `32`  |   `2`   |     | `82` | `52`  |  `R`  |     | `114` | `72`  |  `r`  |
| `19` | `13`  | `DC3` |     | `51` | `33`  |   `3`   |     | `83` | `53`  |  `S`  |     | `115` | `73`  |  `s`  |
| `20` | `14`  | `DC4` |     | `52` | `34`  |   `4`   |     | `84` | `54`  |  `T`  |     | `116` | `74`  |  `t`  |
| `21` | `15`  | `NAK` |     | `53` | `35`  |   `5`   |     | `85` | `55`  |  `U`  |     | `117` | `75`  |  `u`  |
| `22` | `16`  | `SYN` |     | `54` | `36`  |   `6`   |     | `86` | `56`  |  `V`  |     | `118` | `76`  |  `v`  |
| `23` | `17`  | `ETB` |     | `55` | `37`  |   `7`   |     | `87` | `57`  |  `W`  |     | `119` | `77`  |  `w`  |
| `24` | `18`  | `CAN` |     | `56` | `38`  |   `8`   |     | `88` | `58`  |  `X`  |     | `120` | `78`  |  `x`  |
| `25` | `19`  | `EM`  |     | `57` | `39`  |   `9`   |     | `89` | `59`  |  `Y`  |     | `121` | `79`  |  `y`  |
| `26` | `1A`  | `SUB` |     | `58` | `3A`  |   `:`   |     | `90` | `5A`  |  `Z`  |     | `122` | `7A`  |  `z`  |
| `27` | `1B`  | `ESC` |     | `59` | `3B`  |   `;`   |     | `91` | `5B`  |  `[`  |     | `123` | `7B`  |  `{`  |
| `28` | `1C`  | `FS`  |     | `60` | `3C`  |   `<`   |     | `92` | `5C`  |  `\`  |     | `124` | `7C`  | `\|`  |
| `29` | `1D`  | `GS`  |     | `61` | `3D`  |   `=`   |     | `93` | `5D`  |  `]`  |     | `125` | `7D`  |  `}`  |
| `30` | `1E`  | `RS`  |     | `62` | `3E`  |   `>`   |     | `94` | `5E`  |  `^`  |     | `126` | `7E`  |  `~`  |
| `31` | `1F`  | `US`  |     | `63` | `3F`  |   `?`   |     | `95` | `5F`  |  `_`  |     | `127` | `7F`  | `DEL` |

</details>

---

### ASCII Limitations

Of course, it should be immediately obvious that this encoding system is
pretty badly broken, since this only includes the primary character set
needed for American English.

Later, an additional 128 characters were added as **Extended ASCII** to
bring into scope accented vowels, ligatures, and some additional
punctuation and symbols.

<details>
<summary>Extended ASCII Table</summary>

|   Dec |  Hex  | Char  |     |   Dec |  Hex  | Char  |     |   Dec |  Hex  | Char  |     |   Dec |  Hex  | Char  |
| ----: | :---: | :---: | --- | ----: | :---: | :---: | --- | ----: | :---: | :---: | --- | ----: | :---: | :---: |
| `128` | `80`  |  `€`  |     | `160` | `A0`  |       |     | `192` | `C0`  |  `À`  |     | `224` | `E0`  |  `à`  |
| `129` | `81`  |       |     | `161` | `A1`  |  `¡`  |     | `193` | `C1`  |  `Á`  |     | `225` | `E1`  |  `á`  |
| `130` | `82`  |  `‚`  |     | `162` | `A2`  |  `¢`  |     | `194` | `C2`  |  `Â`  |     | `226` | `E2`  |  `â`  |
| `131` | `83`  |  `ƒ`  |     | `163` | `A3`  |  `£`  |     | `195` | `C3`  |  `Ã`  |     | `227` | `E3`  |  `ã`  |
| `132` | `84`  |  `„`  |     | `164` | `A4`  |  `¤`  |     | `196` | `C4`  |  `Ä`  |     | `228` | `E4`  |  `ä`  |
| `133` | `85`  |  `…`  |     | `165` | `A5`  |  `¥`  |     | `197` | `C5`  |  `Å`  |     | `229` | `E5`  |  `å`  |
| `134` | `86`  |  `†`  |     | `166` | `A6`  |  `¦`  |     | `198` | `C6`  |  `Æ`  |     | `230` | `E6`  |  `æ`  |
| `135` | `87`  |  `‡`  |     | `167` | `A7`  |  `§`  |     | `199` | `C7`  |  `Ç`  |     | `231` | `E7`  |  `ç`  |
| `136` | `88`  |  `ˆ`  |     | `168` | `A8`  |  `¨`  |     | `200` | `C8`  |  `È`  |     | `232` | `E8`  |  `è`  |
| `137` | `89`  |  `‰`  |     | `169` | `A9`  |  `©`  |     | `201` | `C9`  |  `É`  |     | `233` | `E9`  |  `é`  |
| `138` | `8A`  |  `Š`  |     | `170` | `AA`  |  `ª`  |     | `202` | `CA`  |  `Ê`  |     | `234` | `EA`  |  `ê`  |
| `139` | `8B`  |  `‹`  |     | `171` | `AB`  |  `«`  |     | `203` | `CB`  |  `Ë`  |     | `235` | `EB`  |  `ë`  |
| `140` | `8C`  |  `Œ`  |     | `172` | `AC`  |  `¬`  |     | `204` | `CC`  |  `Ì`  |     | `236` | `EC`  |  `ì`  |
| `141` | `8D`  |       |     | `173` | `AD`  |       |     | `205` | `CD`  |  `Í`  |     | `237` | `ED`  |  `í`  |
| `142` | `8E`  |  `Ž`  |     | `174` | `AE`  |  `®`  |     | `206` | `CE`  |  `Î`  |     | `238` | `EE`  |  `î`  |
| `143` | `8F`  |       |     | `175` | `AF`  |  `¯`  |     | `207` | `CF`  |  `Ï`  |     | `239` | `EF`  |  `ï`  |
| `144` | `90`  |       |     | `176` | `B0`  |  `°`  |     | `208` | `D0`  |  `Ð`  |     | `240` | `F0`  |  `ð`  |
| `145` | `91`  |  `‘`  |     | `177` | `B1`  |  `±`  |     | `209` | `D1`  |  `Ñ`  |     | `241` | `F1`  |  `ñ`  |
| `146` | `92`  |  `'`  |     | `178` | `B2`  |  `²`  |     | `210` | `D2`  |  `Ò`  |     | `242` | `F2`  |  `ò`  |
| `147` | `93`  |  `“`  |     | `179` | `B3`  |  `³`  |     | `211` | `D3`  |  `Ó`  |     | `243` | `F3`  |  `ó`  |
| `148` | `94`  |  `”`  |     | `180` | `B4`  |  `´`  |     | `212` | `D4`  |  `Ô`  |     | `244` | `F4`  |  `ô`  |
| `149` | `95`  |  `•`  |     | `181` | `B5`  |  `µ`  |     | `213` | `D5`  |  `Õ`  |     | `245` | `F5`  |  `õ`  |
| `150` | `96`  |  `–`  |     | `182` | `B6`  |  `¶`  |     | `214` | `D6`  |  `Ö`  |     | `246` | `F6`  |  `ö`  |
| `151` | `97`  |  `—`  |     | `183` | `B7`  |  `·`  |     | `215` | `D7`  |  `×`  |     | `247` | `F7`  |  `÷`  |
| `152` | `98`  |  `˜`  |     | `184` | `B8`  |  `¸`  |     | `216` | `D8`  |  `Ø`  |     | `248` | `F8`  |  `ø`  |
| `153` | `99`  |  `™`  |     | `185` | `B9`  |  `¹`  |     | `217` | `D9`  |  `Ù`  |     | `249` | `F9`  |  `ù`  |
| `154` | `9A`  |  `š`  |     | `186` | `BA`  |  `º`  |     | `218` | `DA`  |  `Ú`  |     | `250` | `FA`  |  `ú`  |
| `155` | `9B`  |  `›`  |     | `187` | `BB`  |  `»`  |     | `219` | `DB`  |  `Û`  |     | `251` | `FB`  |  `û`  |
| `156` | `9C`  |  `œ`  |     | `188` | `BC`  |  `¼`  |     | `220` | `DC`  |  `Ü`  |     | `252` | `FC`  |  `ü`  |
| `157` | `9D`  |       |     | `189` | `BD`  |  `½`  |     | `221` | `DD`  |  `Ý`  |     | `253` | `FD`  |  `ý`  |
| `158` | `9E`  |  `ž`  |     | `190` | `BE`  |  `¾`  |     | `222` | `DE`  |  `Þ`  |     | `254` | `FE`  |  `þ`  |
| `159` | `9F`  |  `Ÿ`  |     | `191` | `BF`  |  `¿`  |     | `223` | `DF`  |  `ß`  |     | `255` | `FF`  |  `ÿ`  |

</details><br>

The upper 128 values, often called **ASCII (Upper Half)**, extended ASCII to 8
bits, but it was never standardized as a single character set. Different systems
filled the upper half in differently, and to this day there are differences from
system to system in how these characters are implemented.

Furthermore, this was still Euro- and mostly Anglo-centric. The character set
did not contain any non-European characters (like Cyrillic, Hebrew, Arabic,
Chinese, Japanese, etc.) and was even lacking characters for some European
languages like Greek.

---

### The Dawn of Unicode

After the arrival of ASCII and other English character encodings like EBCDIC
(Extended Binary-Coded Decimal Interchange Code), the computing world went
through a phase where there were literally hundreds of character encodings in
use, each with its own ISO (International Organization for Standardization)
standard, and it was necessary to indicate which encoding page was in use for
any text block in order to properly render content.

A group of engineers began work in the 1980s on a 16-bit universal encoding
that could encompass all living languages, and in 1991 the Unicode Consortium
was founded. They published a 16-bit Unicode character set in 1991.

By 1996, Unicode had moved past 16 bits with version 2.0, but the 16-bit set
(known as UCS-2) already covered most characters in use. See
[this overview of UCS-2](https://www.columbia.edu/kermit/ucs2.html) for more.

Of course, this still left a couple of problems.

First, this is wasteful, since it encodes every character as 16 bits, even when
most are unnecessary (almost the entirety of this document is written in the
7-bit characters available in ASCII for instance).

And second, common operating systems, like Windows 95, were built before Unicode
was widely supported.

---

### UTF-8 Fixes the Problems

Because there was a necessary period of conversion between pre- and
post-Unicode systems, there was an opportunity to address the limitations of
UCS-2 before full adoption.

**UTF-8** (Unicode Transformation Format: 8-bit) is a variable-length encoding
standard in which the smallest unit size is 8 bits. In order to accommodate
the complete Unicode set, a character can use one, two, three, or four of these
units.

This ensures that all character sets can be handled but also that bytes of
memory won't be wasted when not needed for the most common characters.

Importantly, UTF-8 ensured backward compatibility with ASCII by encoding 8-bit
characters to the same values used in ASCII.

---

### Python Uses the System Default Encoding

Given that the vast majority of text is still ASCII-encodable, many systems can
read plain ASCII text without any trouble. But Python doesn't assume ASCII. When
you open a file without specifying an encoding, Python uses your system's default
encoding.

On many Windows computers, that default is `cp1252`, which is why the errors below
mention `cp1252`. Other systems use a different default, so the same code can
behave differently on another computer.

Specifying the encoding yourself removes that guesswork.

---

### Non-ASCII Characters in Files

For this example, I have provided the following text file:  
• [moby_dick.txt](./Files/moby_dick.txt)

If you review the file itself, on lines 353 to 357, you'll find the following
text:

```
  “While you take in hand to school others, and to teach them by what
  name a whale-fish is to be called in our tongue, leaving out, through
  ignorance, the letter H, which almost alone maketh up the
  signification of the word, you deliver that which is not true.”
  —_Hackluyt._
```

The first character of the last line is an em-dash, not a hyphen. This
character does not exist in ASCII.

There are more instances of this character, but only the first one matters to
our code as you'll see momentarily.

---

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Unicode Errors Reading Files

If we use our typical code to read the file...

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_name = "moby_dick.txt"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

with open(file_path) as f:
    contents = f.read()
    print(len(contents))
```

We'll encounter a `UnicodeDecodeError`.

Output:

```
Traceback (most recent call last):
  File "...\09_bonus_ascii_and_utf8.py", line 20, in <module>
    contents = f.read()
               ^^^^^^^^
  File "...\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 6589: character maps to <undefined>
```

The code file has this example commented out, so the rest of the file can run.
Uncomment it to see the error for yourself.

---

### Fixing the Errors with `encoding="UTF-8"`

We can resolve this error by specifying the encoding type as UTF-8 when we
open the file.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_name = "moby_dick.txt"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

with open(file_path, encoding="UTF-8") as f:
    contents = f.read()
    print(len(contents))
```

Output:

```
1238254
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Unicode Errors Reading Files

If we use our typical code to read the file...

```python
from relative_paths import get_path
from pathlib import Path

file_name = "moby_dick.txt"
file_path = get_path(file_name, "Files")
file = Path(file_path)
contents = file.read_text()
print(len(contents))
```

We'll encounter a `UnicodeDecodeError`.

Output:

```
Traceback (most recent call last):
  File "...\09_bonus_ascii_and_utf8.py", line 37, in <module>
    contents = file.read_text()
               ^^^^^^^^^^^^^^^^
  File "...\pathlib.py", line 1059, in read_text
    return f.read()
           ^^^^^^^^
  File "...\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 6589: character maps to <undefined>
```

The code file has this example commented out, so the rest of the file can run.
Uncomment it to see the error for yourself.

---

### Fixing the Errors with `encoding="UTF-8"`

We can resolve this error by specifying the encoding type as UTF-8 when we
call `read_text()`, which opens the file under the covers.

```python
from relative_paths import get_path
from pathlib import Path

file_name = "moby_dick.txt"
file_path = get_path(file_name, "Files")
file = Path(file_path)
contents = file.read_text(encoding="UTF-8")
print(len(contents))
```

Output:

```
1238254
```

</details>

---
