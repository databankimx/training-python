## Bonus: Virtual Environments

Now that we've learned how to import a module, the next step will be to import 
functionality from external libraries that we did not write ourselves.

Some of these libraries require installation.

Different projects will require different libraries to be installed, and it's 
important to keep track of what we're installing.

It's not a good idea to just use your local machine's instance of Python and 
install everything there, because there would be no way to identify what is
used by which project.

Knowing what a given project uses is important, since Python provides a means 
of creating a *requirements.txt* file that lists all the libraries that must be
installed when deploying your project to another machine.

---

### Create a Virtual Environment

Instead, it is preferable to create a virtual environment (venv) and install 
only the libraries needed for your project.

Here's how we do that.

1. Open the project folder in VS Code
2. Launch a terminal if one is not already open
3. Create the virtual environment (venv) by running the following command in 
   your terminal:  
   `python -m venv .venv`
   * This will create a virtual environment called `.venv` in your project 
     folder.
   * It's not necessary to call it .venv (you can name it whatever you want), 
     but it's customary

The newly created virtual environment contains its own complete installation 
of Python.

---

### Activate the Virtual Environment

When the virtual environment is inactive, you are still using your local 
machine's Python instance, so it's important to activate it.

Here's how:

1. Run the following command in your terminal  
   `.venv\scripts\activate`
   * After this runs, your terminal prompt should show (.venv) at the left
   * If you named yours something other than `.venv`, then the name you used 
     should be substituted in the command and will appear in the terminal 
     prompt
   * You can run the command `deactivate` to deactivate the virtual 
     environment at any time

---

### Make Sure the Virtual Environment Interpreter is Selected

In Visual Studio Code, you need to ensure that the Python interpreter used
for code testing is the one in the virtual environment.

1. Open the VS Code Command Palette by doing one of the following:
    * Click the cog icon in the lower left and select "Command Palette"  
      or
    * Press `CTRL`+`SHIFT`+`P`
2. Select "Python: Select Interpreter" from the menu
3. Select the interpreter associated with your virtual environment

---

### Update the Virtual Environment and Install Libraries

The PIP installer will likely be out of date in your virtual environment, so
you should update it using the following command:

```
python.exe -m pip install --upgrade pip
```

After that, you can install whatever libraries you need to the virtual environment using the following command:

```
python.exe -m pip install library_name
```

---

### Creating a Requirements File

After you have developed an application, you will need to deploy it,
typically to a server other than where you wrote the code.

This means that the server will automatically need to have the same modules
installed that you used for testing.

To make this easier, you can create a requirements file using the following
command:

```pwsh
python -m pip freeze > requirements.txt
```

... which will create a file called `requirements.txt` in which all of the
installed module dependencies are listed, like this:

```
colorama==0.4.6
iniconfig==2.0.0
packaging==24.1
pluggy==1.5.0
pygame==2.6.0
pytest==8.3.2
```

---
