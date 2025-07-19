💓 Pulse CRM

Pulse CRM is a sleek, responsive customer relationship management web application built with Flask, MySQL, and Bootstrap. It allows users to manage customer data with an intuitive interface and full CRUD (Create, Read, Update, Delete) functionality.

🌟 Features

- 🧾 View all customers in a styled, paginated table
- ➕ Add new customers through a form
- ✏️ Edit existing customer details
- 🗑️ Delete customers
- 💬 Flash messages for actions (add/update/delete)
- 💅 Bootstrap-powered UI with custom CSS for a modern look
- 📁 Environment variable support with `.env`

🛠️ Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Backend   | Python, Flask      |
| Database  | MySQL              |
| Frontend  | HTML, CSS, Bootstrap |
| Hosting   | Localhost (can be deployed via Render/Railway) |


🔧 Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/your-username/pulse-crm.git
cd pulse-crm

2. Set Up a Virtual Environment
bash -
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies
bash
pip install -r requirements.txt

4. Set Environment Variables

Create a .env file in the root directory and add:
DB_HOST=your-db-host
DB_PORT=3306
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_NAME=your-db-name

5. Run the App
bash -
python app.py
Then go to: http://127.0.0.1:5000

🗃️ Database Setup
Create the customers table using the following SQL:

sql
Copy
Edit
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    company VARCHAR(100),
    notes TEXT
);

-------------------------------------

🙋‍♀️ Author
Nashita Kausar
💼 LinkedIn - @nashitakausar
📫 Email - kausarna@mail.uc.edu
