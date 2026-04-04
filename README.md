# Library Management System with Data Analysis & Power BI Dashboard

## Project Overview
This project is a **Library Management System** built using **Python and MySQL**, enhanced with **data analysis features** and a **Power BI dashboard** for visualization.

The system allows users to:
- Borrow and return books
- Track book availability
- Calculate overdue fines
- Analyze borrowing patterns
- Visualize insights using Power BI


## Tech Stack
- **Python** – Core application logic
- **MySQL** – Database management
- **mysql-connector-python** – Database connectivity
- **Power BI** – Data visualization dashboard


## Database Design

### Tables Used:
- **books**
  - book_id (Primary Key)
  - book_name
  - available
  - category

- **borrowed_books**
  - borrow_id (Primary Key)
  - book_id (Foreign Key reference)
  - username
  - borrow_date
  - due_date
  - return_date


## Features

### Book Management
- Display all books
- Display available books

### Borrow & Return System
- Borrow a book with due date tracking
- Return a book with overdue fine calculation

### Data Analysis (Python)
- Top 3 most borrowed books
- Most active users
- Overdue books count
- Average borrowing duration

### Power BI Dashboard
- Total borrows
- Unique books count
- Category distribution
- Book borrowing comparison
- Filters by category and users

---

## Power BI Insights
The dashboard provides:
- Visual summary of borrowing trends
- Category-wise distribution
- User activity analysis
- Comparative book popularity

---

## How to Run the Project

### 1. Setup Database
- Import `library_db.sql` into MySQL

### 2. Install Dependencies
```bash
pip install mysql-connector-python

### 3. Run the python file:
   python library.py
### 4. Open the Power BI Dashboard
   Open Library_dashboard.pbix in Power BI Desktop   
