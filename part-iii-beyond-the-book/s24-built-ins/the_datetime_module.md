## The `datetime` Module

Dates and times look simple, but calendars have month lengths, leap years, and
time zones. The `datetime` module handles that work for you, so use it rather than
doing arithmetic on numbers by hand.

The module provides three classes used most often here:

* `date`: a calendar date, with no time
* `datetime`: a date and a time together
* `timedelta`: a length of time, such as 30 days

The code for this lesson is in [the_datetime_module.py](./the_datetime_module.py):

```python
from datetime import date, datetime, timedelta

launch = date(2024, 3, 15)
print(launch)
print(launch.strftime("%d %B %Y"))
print(launch + timedelta(days=30))

meeting = datetime(2024, 3, 15, 14, 30)
print(meeting.isoformat())
print(meeting.strftime("%A, %H:%M"))

days_between = date(2024, 12, 25) - launch
print(days_between.days)
```

---

### Creating and Printing Dates

Pass the year, month, and day to `date()`. Printing a `date` shows the ISO format,
`YYYY-MM-DD`. The `strftime()` method formats it with a pattern of your choice:

```python
launch = date(2024, 3, 15)
print(launch)
print(launch.strftime("%d %B %Y"))
```

Output:

```
2024-03-15
15 March 2024
```

Common codes for `strftime()` are `%Y` for the four-digit year, `%m` for the
month number, `%B` for the month name, `%d` for the day, `%A` for the weekday
name, `%H` for the hour, and `%M` for the minute.

---

### Adding a Duration

Adding a `timedelta` moves a date forward or back. Adding 30 days to 15 March
gives 14 April, because March has 31 days:

```python
print(launch + timedelta(days=30))
```

Output:

```
2024-04-14
```

`timedelta` also accepts `hours`, `minutes`, and `seconds`.

---

### Working with Date and Time

A `datetime` holds the time as well. `isoformat()` gives a standard text form, and
`strftime()` works the same way as for dates:

```python
meeting = datetime(2024, 3, 15, 14, 30)
print(meeting.isoformat())
print(meeting.strftime("%A, %H:%M"))
```

Output:

```
2024-03-15T14:30:00
Friday, 14:30
```

This `datetime` has no time zone attached. Lessons on time zones need the
`zoneinfo` module, which this one doesn't cover.

---

### Subtracting Dates

Subtracting one date from another gives a `timedelta`. Its `days` attribute is the
number of whole days between them:

```python
days_between = date(2024, 12, 25) - launch
print(days_between.days)
```

Output:

```
285
```

---

### Try It

Pick a date of your birthday in this year, and use `datetime` to find the
weekday it falls on. Then use `timedelta` to find the date 100 days later.

---
