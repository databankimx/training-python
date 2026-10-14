## The String `.format()` Function

In v2.6, as an improvement on the somewhat cumbersome string-modulo operator,
Python introduced the `.format()` method for the `str` type.

With the `.format()` method, we use curly brace pairs `{}` as the 
placeholders (removing the requirement to specify type, which was never 
enforced in the first place). Arguments to the function are expressions, which will replace the curly braces in the resulting string at:

* [The index indicated in the braces](./03_format_indices.md):  
  ```python
  "{0} {1}".format(arg_0, arg_1)
  ```
* [The keyword indicated in the braces](./04_format_keywords.md):   
  ```python
  "{arg_1} {arg_2}".format(arg_1=val_1, arg_2=val_2)
  ```
* [The order of appearance if the braces are left empty](./05_format_auto.md).
  ```python
  "{} {}".format(first_arg, second_arg)
  ```

---
