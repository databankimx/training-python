## Enumeration Methods

We can add methods to an enum just like an ordinary class.

Looking at our `Weekday` enum, we might want to be able to select a
variant based on a specific date.

----

### Adding a Method

We can add a method to perform that task, like this:

```python
from enum import Enum
from datetime import date

class Weekday(Enum):
    """Defines names for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def from_date(cls, date: date) -> Enum:
        """Get weekday name of the given date"""
        return cls(date.isoweekday())
```

Two notes:

* We are declaring this as a `@classmethod`, because we will never be
  creating instance variables, so this runs on the type.
* I am using the `date.isoweekday()` instead of `date.weekday()` because
  the former uses values 1 to 7, which matches our variant values as
  opposed to 0 to 6 in the latter. I could have used
  `date.weekday() + 1`

---

### Using the Enum Method

Now, we can use that method to extract the proper variant:

```python
day = Weekday.from_date(date.today())
print(f"Today is {day.name.title()}.")
```

Output:

```
Today is Wednesday.
```

... Your day may vary, of course

---
