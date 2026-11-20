import sqlite3
conn = sqlite3.connect('company.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Employees")
cursor.execute("""
CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Department TEXT,
    JobTitle TEXT,
    Salary INTEGER,
    HireDate TEXT
)
""")
employees_data = [
    (101, 'Aarav', 'Sharma', 'Engineering', 'Software Developer', 85000, '2022-03-15'),
    (102, 'Priya', 'Patel', 'Marketing', 'Marketing Manager', 72000, '2021-07-10'),
    (103, 'Rohan', 'Verma', 'Sales', 'Sales Executive', 55000, '2023-01-20'),
    (104, 'Ananya', 'Nair', 'Engineering', 'Data Analyst', 78000, '2022-11-05'),
    (105, 'Vikram', 'Singh', 'HR', 'HR Specialist', 60000, '2020-09-12'),
    (106, 'Meera', 'Iyer', 'Finance', 'Accountant', 68000, '2021-05-18')
]
cursor.executemany("""
INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, JobTitle, Salary, HireDate)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", employees_data)
conn.commit()
print("--- All Employees ---")
for row in cursor.execute("SELECT * FROM Employees"):
    print(row)
print("\n--- Salary > 70,000 ---")
for row in cursor.execute("SELECT FirstName, LastName, Department, Salary FROM Employees WHERE Salary > 70000"):
    print(row)
print("\n--- Engineering Department ---")
for row in cursor.execute("SELECT * FROM Employees WHERE Department = 'Engineering'"):
    print(row)
print("\n--- Sorted by Salary (Highest to Lowest) ---")
for row in cursor.execute("SELECT FirstName, LastName, JobTitle, Salary FROM Employees ORDER BY Salary DESC"):
    print(row)
cursor.execute("UPDATE Employees SET Salary = 62000 WHERE EmployeeID = 103")
conn.commit()
print("\n--- Updated Record (EmployeeID 103) ---")
for row in cursor.execute("SELECT * FROM Employees WHERE EmployeeID = 103"):
    print(row)
conn.close()
