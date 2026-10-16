# Qt WebEngine spike

A separate, throwaway prototype. It doesn't change the current lesson runner.

It shows four Bitwise Operations lessons in one Qt window, rendered with:

- **markdown-it-py** for Markdown, including tables and the lesson's own `<style>` block
- **MathJax** for `$...$` maths
- **Prism** for Python code blocks

## Setup (once)

The spike loads MathJax and Prism from a local `vendor` folder, so it works
offline. This needs Node.js (for npm):

```pwsh
cd C:\Development\training\training-python\lesson-runner-qt-spike\vendor
npm init -y
npm install mathjax@3 prismjs@1
```

Then run the spike:

```pwsh
cd C:\Development\training\training-python\lesson-runner-qt-spike
python -m pip install -r requirements.txt
python spike.py
```

The terminal should now print `MathJax typeset done` instead of `MathJax not loaded`.

## Running it

The spike opens a Qt window. MathJax and Prism load from the `vendor` folder.

## What to check

1. **Tables:** the binary tables in *Binary addition* and *Intuitive but wrong*
   should align, and the lesson's `<style>` block should apply.
2. **Maths:** the `$255+1=0$` and `$1234$` expressions should be typeset.
3. **Code blocks:** rounded corners, margins, and Python highlighting.
4. **Inline code, headings, and links:** compare with the current runner.
