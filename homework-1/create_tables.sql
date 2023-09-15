CREATE TABLE customers
(
	customer_id VARCHAR(5) PRIMARY KEY,
	company_name VARCHAR(100),
	contact_name VARCHAR(100)
);

CREATE TABLE employees
(
	employee_id INT PRIMARY KEY,
	first_name VARCHAR(100),
	last_name VARCHAR(100),
	title VARCHAR(100),
	birth_date DATE,
	notes TEXT
);

CREATE TABLE orders
(
	order_id INT PRIMARY KEY,
	customer_id VARCHAR(10) REFERENCES customers(customer_id),
	employee_id INT REFERENCES employees(employee_id),
	order_date DATE,
	ship_city VARCHAR(100)
);
