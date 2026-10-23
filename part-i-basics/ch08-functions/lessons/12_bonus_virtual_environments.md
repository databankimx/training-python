## Bonus: Virtual Environments

Now that you know how to import a module, the next step is to import functionality from external
libraries that you didn't write yourself.

Some of these libraries have to be installed first.

Different projects need different libraries, so it's important to keep track of what you install.

It's a bad idea to use your computer's main Python installation for everything. You'd have no way of
telling which project uses which library.

Knowing what a project depends on matters, because Python can list those dependencies in a
*requirements.txt* file. Anyone deploying your project to another machine can install everything from
that file.

---

### Create a Virtual Environment

It's better to create a virtual environment (venv) for each project, and install only the libraries that
project needs.

Here's how:

1. Open the project folder in VS Code
2. Open a terminal, if one isn't already open
3. Create the virtual environment by running this command in the terminal:
   `python -m venv .venv`
   * This creates a virtual environment called `.venv` in your project folder.
   * You don't have to call it `.venv`. You can name it anything you like, but `.venv` is the
     customary choice.

A virtual environment has its own Python launcher and its own set of installed packages. It still uses
your base Python installation to run, but nothing you install inside it affects other projects.

---

### Activate the Virtual Environment

While the virtual environment is inactive, you're still using your computer's main Python, so you need to
activate it.

1. Run this command in the terminal:
   `.venv\Scripts\activate`
   * After it runs, the terminal prompt should show `(.venv)` at the left.
   * If you named your environment something else, use that name in the command. It also appears in the
     prompt.
   * To turn the environment off, run `deactivate`.

---

### Select the Virtual Environment's Interpreter

In Visual Studio Code, make sure the Python interpreter used for running and testing your code is the
one in your virtual environment.

1. Open the Command Palette by doing one of the following:
    * Click the cog icon in the lower left, and select "Command Palette,"
      or
    * Press `CTRL`+`SHIFT`+`P`
2. Select "Python: Select Interpreter" from the menu.
3. Select the interpreter that belongs to your virtual environment.

---

### Update pip and Install Libraries

The pip installer in a new virtual environment is probably out of date, so update it first:

```
python -m pip install --upgrade pip
```

Then install whatever libraries your project needs:

```
python -m pip install library_name
```

---

### Create a Requirements File

After you finish an application, you'll usually deploy it to a server other than the one where you wrote
it.

That server needs the same libraries you used while developing, so you need a list of them.

You can create one with this command:

```pwsh
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
```

This creates a file called `requirements.txt` that lists every installed library and its version, like this:

```
colorama==0.4.6
iniconfig==2.0.0
packaging==24.1
pluggy==1.5.0
pygame==2.6.0
pytest==8.3.2
```

> **Why `Out-File -Encoding utf8`?** In Windows PowerShell 5.1, the plain `>` redirect saves the file in
> UTF-16 encoding. pip usually reads that without trouble, but many other tools expect plain UTF-8, so
> writing the file as UTF-8 keeps it portable.

---

### Install from an Existing Requirements File

The requirements file works in the other direction too. When you open a project that someone else has
shared, or set up a fresh venv on a new machine, you can install everything the project needs in one step.

Create and activate the new virtual environment as before, then run:

```pwsh
python -m pip install -r requirements.txt
```

Pip reads each line of the file and installs that exact version of each library. Because the versions are
pinned, the new environment matches the one the project was built with. Run that command from the folder
that contains `requirements.txt`, or give pip the full path to the file.

---
