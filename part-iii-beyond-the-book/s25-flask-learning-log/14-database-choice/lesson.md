# Choosing a Database

## What this step does

The Learning Log has used SQLite since the first step. SQLite stores everything in one file, which is ideal for learning, because it needs no server
and no setup. Real sites often use a database server instead, such as SQL Server or MySQL, so the data lives apart from the app.

This step explains how the switch works. It's information only: nothing in the app changes, and you don't have to change anything to finish the chapter.
The app stays on SQLite unless you choose otherwise.

## Why the switch is simple

SQLAlchemy does the work. The models describe the tables in Python, and the database is chosen by one value, the connection string. The rest of the app
(the routes, the forms, the templates and the tests) never mentions the database, so it doesn't change.

A connection string says what kind of database to use, where it is, and how to log in. It has the same shape for every database, with the database type
first:

- **SQLite (the default):** `sqlite:///learning_log.db`. The file is named after the three slashes. Nothing else is needed.
- **SQL Server:** `mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes`
- **MySQL:** `mysql+pymysql://user:password@server:3306/database`

The `user` and `password` are the login for that database. The `server` is its address, and `database` is the name of the database inside it.

## What you need for each database

Each database needs a driver, which is a small library that lets Python talk to it. The driver is installed into the chapter's virtual environment, in the
same way as Flask:

- **SQL Server:** the `pyodbc` package, plus Microsoft's **ODBC Driver 18 for SQL Server**, installed on the computer.
- **MySQL:** the `PyMySQL` package. No other program is needed.

The chapter's requirements file doesn't include either driver, because most learners won't use them. Install one only if you're using that database:

```pwsh
.venv\Scripts\python.exe -m pip install pyodbc
.venv\Scripts\python.exe -m pip install PyMySQL
```

Run these from the `web-applications` folder.

## Keeping the connection string private

A connection string contains a password, so treat it like one:

- **Don't save it in a file in the project.** The project can be shared or committed to Git.
- **Set it for one PowerShell session only.** The variable disappears when the window closes.

```pwsh
$env:DATABASE_URL = "mysql+pymysql://user:password@server:3306/database"
```

With the variable set in that window, the build creates the tables on that database when you run it from the same window. Run `python build_stage.py s25 14` from
the `web-applications` folder, not from the runner. The runner doesn't read variables set in a PowerShell window.

The tests always use a separate in-memory database, so they never touch the database you point the app at.

## Things to know before you switch

- **The tables are created the same way.** `init-db` creates them on any of the three databases, and the seed data loads in the same way.
- **Existing data isn't moved.** Switching the connection string starts a new, empty database. Moving the SQLite data across is a separate task.
- **The server must be reachable.** A database on another machine needs a network route to it, and the login must have permission to create tables.
- **Only the connection string changes.** You don't edit the models or the routes.

## Testing this step

This step has no new code and no new tests. The build runs the 62 tests from step 13, against SQLite, as before.

## Output

None. This step is information only.

## Changed files

None.

---
