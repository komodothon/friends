# Friends

## Overview of the Project
1. To set up a flask web application to perform CRUD (Create, Read, Update, Delete) operations on a database. 
2. To display database contents and columns as individual cards on page, instead of a table.

## Tools employed
1. Python, flask, html, css, sqlite, bootstrap and font awesome

## Deployment
Currently deployed at https://friends-3yk3.onrender.com

## Code Structure


- **`friends/`**: Contains all source code files.
  - **`App.py`**: Flask application
  - **`setup_db.py`**: Setup of database with sample data. (run this first)
  
- **`instance/`**: Instance folder contains the database file
  - **`friends.db`**: Database file holding information.

- **`templates/`**: HTML files that are served directly.
  - **`layout.html`**: Layout template for alll html files. 
  - **`home.html`**: Main HTML file.

- **`static/`**: Contains static files.
  - **`css/`**: Contains CSS files for styling.
    - **`styles.css`**: Main stylesheet.

- **`.gitignore`**: Specifies files and directories that should be ignored by Git.
- **`README.md`**: Documentation file for the project.


## Acknowledgements
inspired by 
1. https://www.youtube.com/watch?v=tWHXaSC2T_s
2. https://www.youtube.com/watch?v=PppslXOR7TA