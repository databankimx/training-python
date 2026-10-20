## Step 5: Upload the Project

At last, we're ready to upload the project

---

### 5.1: Upload to Test PyPI

To upload the project, we'll run the following command:

```
python.exe -m twine upload --repository testpypi dist/*
```

Note: If uploading to production PyPI, you can omit the `--repository`
switch and value.

When prompted for a username, enter `__token__`  
When prompted for a password, paste the API token you saved in step 2.3

... And that's it! Your project is live in the world!

---

### 5.2: Test and Verify

#### Install Your Module

To verify that you successfully uploaded the project, you can run the 
following command:

```
python.exe -m pip install --index-url https://test.pypi.org/simple/ --no-deps your_project_name
```

Note: If you uploaded to production, the command will omit both the
`--index-url` and `--no-deps` switches, like this:

```
python.exe -m pip install your_project_name
```

---

#### Import Your Module

Now, in a Python file, you can add the following and make sure you can use
your library:

```python
from your_project_name import *
```

---
