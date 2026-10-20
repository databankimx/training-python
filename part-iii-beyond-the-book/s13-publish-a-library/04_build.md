## Build the Package

Before we can upload, the package must be built.

---

### 4.1: Build the Project Files

To build the project, with the terminal pointing to your `main_folder`,
run the following command:

```
python.exe -m build
```

Once that is completed, a new folder called `dist` will be added to the 
directory structure containing the source archive (`tar.gz`) and the `wheel` versions of your 
module for upload:

```
    main_folder/
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── dist/
    │   ├── project_name-version-none-any.whl
    │   └── project_name-version.tar.gz
    ├── src/
    │   └── your_project_name/
    │       ├── __init__.py
    │       └── your_project_name.py
    └── tests/
```

---
