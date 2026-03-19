# Library Management System (Python + MySQL)

## Description
This is an improved version of my previous Library Management System. The earlier version was file-based, and this upgrade introduces MySQL integration along with better data handling and additional features.

---

## Features
- Add, remove, and search books  
- Issue and return system  
- Due date tracking  
- Fine calculation for late returns  
- MySQL database integration  
- Borrowing history tracking  

---

## Tech Stack
- Python  
- MySQL  
- mysql-connector-python  

---

## Improvements Over Previous Version
- Migrated from file-based storage to MySQL database  
- Improved data consistency using relational tables  
- Added fine calculation logic  
- Added borrowing history tracking  
- Improved scalability and structure  

---

## How to Run
1. Import `library_db.sql` into MySQL Workbench  
2. Install dependency:
   ```bash
   pip install mysql-connector-python
3. Run library.py
