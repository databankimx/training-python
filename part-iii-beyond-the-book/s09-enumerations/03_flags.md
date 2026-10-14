## Enum Flags

Inheriting the `Flag` class instead of `Enum` allows us to create enum
variants that represent bit-flags.

When using bit-flags, all variant values must be unique powers of two,
since each represents a single bit in a binary integer. See the topic
on [Bitwise Operations](../S05_Bitwise_Operations/00_warning.md) for
more information.

---

### Creating a Flag Enum

Let's convert our `Weekday` enum to a flag enum.

```python
from enum import Flag

class Weekday(Flag):
    """Defines names for days of the week as bit-flags"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64

    @classmethod
    def from_date(cls, date: date) -> Flag:
        """Get weekday name of the given date"""
        return cls(2 ** date.weekday())
```

> Note: I have modified the `from_date()` method to use a power of two.

We can still access the values as normal:

```python
today = Weekday.from_date(date.today())
print(f"Today is {today.name.title()}.\n")

first_weekday = Weekday.MONDAY
print(first_weekday, first_weekday.value)
```

Output:

```
Today is Wednesday.

MONDAY 1
```

So what's different about this?

---

### Combining Using Bitwise OR

With flags, because each variant is a specific bit value, we can use 
the bitwise OR operator `|` to combine multiple variants.

Here, we'll create a `weekend` variable that includes both
`Weekday.SATURDAY` and `Weekday.SUNDAY`

```python
weekend = Weekday.SATURDAY | Weekday.SUNDAY
print(weekend, weekend.value)
```

Output:

```
Weekday.SATURDAY|SUNDAY 96
```

---

### Combining Numerically

Of course, we can also create a combination just by using the numerical 
value of the combined days.

We know that `Weekday.MONDAY` is 1 and `Weekday.Friday` is 17.

So, we can get `Weekday.MONDAy|FRIDAY` rhis way:

```python
first_last_weekdays = 17
print(Weekday(first_last_weekdays))
```

Output:

```
Weekday.MONDAY|FRIDAY
```

---

### Using Combined Variants

We can use these combined variants in logic and loops. Loops in 
particular provide a special feature of the `Flags` type.

```python
    today = Weekday.from_date(date.today())

    in_weekend = today & weekend == today
    infix = "" if in_weekend else "not "
    print(f"{today.name.title()} is {infix}part of the weekend.\n")

    print("Weekend Days:")
    for day in weekend:
        print(f" - {day.name.title()}")
    print()
```

Output:

```
Wednesday is not part of the weekend.

Weekend Days:
 - Saturday
 - Sunday
```

We use a bitwise AND `&` to check if today is a member of the `weekend`
combination.

---

### Binding Variant Groups to Other Variables

We can use combined values to set up something like a chores tracker.

Here's a function that checks a `chores` dictionary for the appropriate
days:

```python
def show_chores(chores: dict[str: Flag], day: Flag) -> None:
    """Show chores for a given day"""
    print(f"Chores for {day.name.title()}:")
    for chore, days in chores.items():
        if day in days:
            print("-", chore)
```

If we define a chores schedule, we can access it for a given day:

```python
my_chores = {
    "feed the dog": Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
    "do the dishes": Weekday.TUESDAY | Weekday.THURSDAY,
    "answer stack overflow questions": Weekday.MONDAY | Weekday.SATURDAY,
}
            
show_chores(my_chores, Weekday.MONDAY)
```

Output:

```
Chores for Monday:
- feed the dog
- answer stack overflow questions
```

---
