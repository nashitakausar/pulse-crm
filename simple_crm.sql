CREATE DATABASE simple_crm;
USE simple_crm;
CREATE TABLE customers (customer_id INT auto_increment PRIMARY KEY,
						customer_name VARCHAR(255) NOT NULL,
                        email VARCHAR(255),
                        phone VARCHAR(50),
                        company VARCHAR(255),
                        notes TEXT);
CREATE TABLE interactions (interaction_id INT auto_increment PRIMARY KEY,
						   customer_id INT,
                           interaction_date DATE,
                           interaction_type VARCHAR(100),
                           summary TEXT,
                           FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE);
