🏡 Vacation Rental Platform

A modern Vacation Rental Web Application where users can explore properties, book stays, and hosts can manage their listings efficiently.
Built with a scalable architecture and clean UI for better user experience.

** 📌 Features **
👤 User Features
🔐 User Registration & Login (OTP verification)
🏠 Browse available vacation properties
🔎 Search & filter properties
📅 Book property with check-in & check-out date
💳 Booking confirmation system
📄 View booking history

** 🧑‍💼 Host Features **
➕ Add new property listing
🖼 Upload property images
📝 Manage property details
📊 Host Dashboard with statistics
📥 View booking requests
✅ Accept / Reject bookings

** 🛠 Admin Features **
👥 Manage users
🏘 Manage properties
📊 Platform analytics
🔒 Secure authentication system
🧰 Tech Stack
---------Frontend-----------
HTML5
CSS3
Bootstrap 5
JavaScript
--------Backend---------
Python
Django Framework
Database
SQLite (Development)
PostgreSQL (Production)
-------Other Tools-----
Git & GitHub
VS Code
Django ORM
REST API (optional)
---------📂 Project Structure--------
vacation_project/
│
├── accounts/          # User authentication
├── listings/          # Property management
├── bookings/          # Booking system
├── templates/         # HTML templates
├── static/            # CSS, JS, Images
├── media/             # Uploaded property images
├── vacation_project/  # Main project settings
│
├── manage.py
└── README.md


⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/your-username/vacation-rental.git
cd vacation-rental
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Run Server
python manage.py runserver

Visit:

http://127.0.0.1:8000/
