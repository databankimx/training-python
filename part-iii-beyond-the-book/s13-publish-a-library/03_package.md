## Assemble the Package

Now we need to put all the files necessary for the project into the
proper hierarchy.

---

### 3.1: Create the Directory Structure

There is a defined, hierarchical structure to the directories for a
project.

The structure for the source code looks like this:

```
main_folder/
└── src/
    └── your_project_name/
        ├── __init__.py
        └── your_project_name.py
```

#### Rules:

* All code files must be placed in a folder named `src`
* The `__init__.py` file must is required and must contain the following:
  ```python
  # The `.` preceding the project name is mandatory
  # `obj_1, obj_2, ...` is a comma delimited list of functions and classes
  from .project_name import obj_1, obj_2, ...
  ```
    * Only objects listed in `__init__.py` will be uploaded in the project

In the case of my example project, `__init__.py` contains this:

```python
from .sm_utils import timer, Timed, root_path, dir_path, file_path, set_path, \
    default_path, RelativePath, run, run_repeat, counter, reset_counter, \
    Counted, pause, clear_terminal
```

> Important Note!
>
> For the remainder of the process, you must ensure that the terminal is
> pointed to the `main_folder` path

---

### 3.2: Add the Package Files

Once the source code is in place, there are several additional files that
must be added into the `main_folder`

```
    main_folder/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src/
    │   └── your_project_name/
    │       ├── __init__.py
    │       └── your_project_name.py
    └── tests/
```

#### Notes:

* `LICENSE` should contain a copy of the license you've selected
  (e.g.: MIT)
    * [Choose a License](https://choosealicense.com/)
* `pyproject.toml` defines the project to be built and uploaded
    * .toml refers to "Tom's Obviously Minimal Language"
    * [The TOML Language](https://toml.io/en/)
* `README.md` is a markdown file (using GIT-flavored markdown)
    * [Markdown Syntax](https://docs.gitlab.com/ee/user/markdown.html)

---

### 3.3: Modify `pyproject.toml`

The `pyproject.toml` file must contain the following

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "your_project_name"
version = "0.0.1"
authors = [
  { name="Your Name", email="your_email@databankimx.com" },
]
description = "Description of your project"
readme = "readme.md"
requires-python = ">=3.10"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
```

You'll need to modify the the `[project] section to match a description
of the project you will be uploading.

In my case, it looks like this:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "sm_utils"
version = "0.2.7"
authors = [
  { name="Scott McLean", email="smclean@databankimx.com" },
]
description = "Utility Scripts"
readme = "readme.md"
requires-python = ">=3.10"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
```

---

### 3.4: Modify `README.md`

At a minimum, your readme file should include:

* Your Package Name (as a heading)
* A description of the project
* Usage instructions

You can review this [README.md](./sm_utils_project/README.md) file as an 
example.

---
