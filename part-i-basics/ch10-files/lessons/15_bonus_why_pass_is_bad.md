## Bonus Lesson - Why `except: pass` is Bad!

I mentioned before that using the `pass` statement is frequently bad form in an
except block, especially in a generic one, where you're not specifying an error
type.

Let's take a look at a concrete example of why:

### Escaping From an Infinite Loop

Here, I am creating an obvious infinite loop. In the real world it will be
more difficult to detect infinite-run conditions, but this illustrates the idea.

```python
i = 0
while True:
    i += 1
    print(f"(iteration {i}) - I'm just gonna run forever...")
```

If we run this code, it will execute forever, and we'll need to use the
`CTRL`+`C` command in the terminal to break the infinite loop.

Output:

```
(iteration 1) - I'm just gonna run forever...
(iteration 2) - I'm just gonna run forever...

...

(iteration 19883) - I'm just gonna run forever...
(iteration 19884) - I'm just gonna run forever...
Traceback (most recent call last):
  File "...\15_bonus_why_pass_is_bad.py", line 10, in <module>
    print(f"(iteration {i}) - I'm just gonna run forever...")
KeyboardInterrupt
```

The code file has the dangerous versions of the loop below commented out, so the
file doesn't hang when you run it. Uncomment one at a time to see its behavior.

---

### Implementing `try` ... `except` the Wrong Way

Now, let's imagine that there is some code in the loop that could cause an
error, but we don't care and just want to skip the current iteration and keep
running. We might (if we were lazy and thoughtless) do that by using `pass` in
the `except:` block:

```python
i = 0
while True:
    try:
        i += 1
        print(f"(iteration {i}) I'm just gonna run forever...")
    except:
        pass
```

Great! We're suppressing the exceptions, but...

Output:

```
(iteration 1) I'm just gonna run forever...
(iteration 2) I'm just gonna run forever...

...

(iteration 19883) I'm just gonna run forever...
(iteration 19884) I'm just gonna run forever...

...
```

The loop continues forever, and `CTRL`+`C` doesn't work!

What gives?

---

### `KeyboardInterrupt` is an Error Type!

As we saw above, when we exit a program using `CTRL`+`C`, it initiates a
traceback where the error type identified is `KeyboardInterrupt`.

So if we're suppressing all error types (as we are with a naked `except:`),
then there is no longer a way to escape from an infinite loop if one occurs.

No matter how many times we press `CTRL`+`C`, the interrupt is suppressed, and
the loop just keeps running.

The only way out would be to kill the `Python.exe` process from Task Manager, or
close the terminal window.

Note that `except Exception:` would not catch `KeyboardInterrupt`. In Python,
`KeyboardInterrupt` inherits from `BaseException`, not from `Exception`. A naked
`except:` catches everything, including `BaseException`, which is why it swallows
the interrupt.

---

### Be Careful Using `pass`

This is not to say that there is never a case where `pass` should be used. If
that was the case, it wouldn't exist in the language.

Rather, I'm saying that you need to be careful:

* Consider any cases where the behavior needs to be different
* Give some indication that you handled an error (either onscreen or in a log)
* Use `pass` only when you're certain that it won't cause unintended behavior.

We can make our code a bit better, like this:

```python
i = 0
while True:
    try:
        i += 1
        print(f"(iteration {i}) - I'm just gonna run forever...")
    except KeyboardInterrupt:
        print("OK... I'll stop... :(")
        break
    except Exception as ex:
        print(ex)
        pass
```

Here, we are considering the impact of a possible infinite loop and the
need for a `KeyboardInterrupt` by handling its error type first.

Then we're handling the catch-all of any other error types, but we're printing
its message before proceeding.

We still use `pass`, but we've protected against the worst case scenario.

Output:

```
(iteration 1) - I'm just gonna run forever...
(iteration 2) - I'm just gonna run forever...

...

(iteration 19883) - I'm just gonna run forever...
(iteration 19884) - I'm just gonna run forever...
OK... I'll stop... :(
```

---

### The Moral of the Story

There are good reasons why it's bad to use `pass` with a naked `except:`
block, so just don't do it!

---
