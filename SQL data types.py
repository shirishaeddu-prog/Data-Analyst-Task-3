import sqlite3

db = sqlite3.connect("shop.db")
c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS sales(id INTEGER, name TEXT, product TEXT, category TEXT, price REAL)")

c.execute("DELETE FROM sales")

data = [
    (1, "Siri", "Laptop", "Electronics", 55000),
    (2, "Rahul", "Mobile", "Electronics", 25000),
    (3, "Anu", "Mouse", "Accessories", 800),
    (4, "Kiran", "Keyboard", "Accessories", 1500)
]

c.executemany("INSERT INTO sales VALUES(?,?,?,?,?)", data)
db.commit()

print("1. Products above 5000:")
c.execute("SELECT product, price FROM sales WHERE price > 5000")
print(c.fetchall())

print("\n2. Products by price:")
c.execute("SELECT product, price FROM sales ORDER BY price DESC")
print(c.fetchall())

print("\n3. Average price:")
c.execute("SELECT AVG(price) FROM sales")
print(c.fetchone()[0])

print("\n4. Sales by category:")
c.execute("SELECT category, SUM(price) FROM sales GROUP BY category")
print(c.fetchall())

print("\n5. Products above average:")
c.execute("SELECT product, price FROM sales WHERE price > (SELECT AVG(price) FROM sales)")
print(c.fetchall())

db.close()

print("\nTask 3 Completed Successfully!") 