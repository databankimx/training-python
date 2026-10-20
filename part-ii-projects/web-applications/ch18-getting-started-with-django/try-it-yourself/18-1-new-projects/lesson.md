# Exercise 18-1: New Projects

## The exercise

To get a better idea of what Django does, build a couple of empty projects and look at what Django creates. Make a new folder
with a simple name, such as `tik_gram` or `insta_tok`, outside your `learning_log` directory. Navigate to that folder in a
terminal, create a virtual environment, install Django, and run the command `django-admin startproject tg_project .`, making
sure to include the dot at the end of the command.

## Running this exercise

This exercise doesn't have code to run. It's about looking at the files Django creates.

1. Open PowerShell in a new folder outside `web-applications`, such as `C:\Training\tik_gram`.
2. Create and activate a virtual environment:

   ```pwsh
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install Django 5.2.17, the same version the chapter uses:

   ```pwsh
   python -m pip install "Django==5.2.17"
   ```

4. Create the project. The dot at the end puts the project in the current folder:

   ```pwsh
   django-admin startproject tg_project .
   ```

5. Look at what was created. Compare it with the `ll_project` folder from chapter 18, step 1. The files are the same, because
   both projects came from the same command.
6. Repeat the steps with a second folder, such as `insta_tok`, until you're comfortable with what Django creates.

## What to look for

- **`manage.py`:** the command-line tool. Every project command goes through it.
- **A folder named after the project (`tg_project`):** the settings, the list of addresses, and the WSGI and ASGI files.
- **The dot at the end of the command:** without it, Django creates an extra folder around the project folder.

## Solution

There's no code to submit. Your check is that each new project has the same files, and that you can explain what each one is for.

## Output

A new folder with `manage.py` and a `tg_project` folder inside it, and nothing more.
