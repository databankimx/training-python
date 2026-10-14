## MySQL Installation and Setup

Before you can proceed with this topic, you'l need to install MySQL.

If you don't already have MySQL installed, here is a Google Drive share where I have stashed the [MySQL Installers](https://drive.google.com/drive/folders/1Pg3IJB8pEMZmM0VXdPFQLXNaOLnq9piZ?usp=drive_link)

---

### MySQL Setup

1. Download and install [MySQL 8.1](https://drive.google.com/file/d/1dHOzAvlspUtxmsafwhtd0rDLAOb3iDXY/view?usp=drive_link)
    * Configure a Username and Password  
      Note: I use Username: *python* | Password: *training* in the lessons
        * You can use the MySQL Configurator application  
          or
        * From the MySQL Command Line Client, run the following:
          ```sql
          CREATE USER 'python'@'localhost' IDENTIFIED BY 'training'
          USE MYSQL
          GRANT ALL ON *.* TO 'python'@'localhost'
          ```
2. Download and install [MySQL Workbench 8.0](https://drive.google.com/file/d/17Try0gyy6Ai0W0ts-SRhLhmXervRp9Gh/view?usp=drive_link)

---

### Python Setup

You'll also need the Python MySQL Connector

1. Create a virtual environment:  
   `python -m venv .venv`

2. Activate the virtual environment:  
   `.venv\Scripts\activate`

3. Install the MySQL Connector module:  
   `python -m pip install mysql-connector-python`

---

### Ready to Go

Once everything is set up, we'll jump right into things.

Move on to [01_connect.md](./01_connect.md)

---
