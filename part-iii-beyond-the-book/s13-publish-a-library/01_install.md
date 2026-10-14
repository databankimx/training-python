## Step 1: Install all Required Modules

To build a project and publish it to PyPI, you'll need to install a
couple of extra modules.

---

### 1.1: Set Up a Virtual Environment

As usual, whenever you'll be installing modules specific to some project,
it is advisable to use a virtual environment in order to avoid including
those Python modules in places where they are unnecessary.

To set up a virtual environment, run the following command:

```
python.exe -m venv .venv
```

To activate the virtual environment, run the following command:

```
.venv\scripts\activate
```

---

### 1.2: Update PIP (optional but recommended)

The virtual environment is generated from the original Python distribution
you're running. Because of this, it's recommended that you update the 
installed PIP (Package Installer for Python).

```
python.exe -m pip install --upgrade pip
```

---

### 1.3: Install the `build` Module

The `build` module is used to create the package that you'll be uploading,
so we'll need to install it.

```
python.exe -m pip install build
```

---

### 1.4: Install the `twine` Module

The `twine` module is used to connect to the PyPI repository and upload
the package generated from `build`, so we'll need it as well.

```
python.exe -m pip install twine
```

---