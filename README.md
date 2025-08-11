# 🌸 Spring Travels - Backend (Django)

This is the **backend server** for the **Spring Travels** application.  
It is built with **Django** and provides RESTful APIs for managing travel routes, bookings, and user data.

---

## 🚀 Features
- **User registration & authentication**
- **Manage travel routes and schedules**
- **Book and manage tickets**
- **Stores data in a relational database** (MySQL / SQLite)
- **CORS enabled** for frontend (React) integration
- **REST API endpoints** using Django REST Framework (if applicable)

---

## 🛠️ Tech Stack
- **Backend Framework:** Django
- **Language:** Python
- **Database:** MySQL / SQLite
- **Authentication:** Django's built-in auth / JWT (if used)
- **Deployment Ready:** Configured for cloud hosting (Render/Heroku)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/spring-travels-backend.git
cd spring-travels-backend
```
2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the project root:

ini
Copy
Edit
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url
5️⃣ Run Migrations
bash
Copy
Edit
python manage.py migrate
6️⃣ Start the Development Server
bash
Copy
Edit
python manage.py runserver
🌐 API Endpoints
Method	Endpoint	Description
GET	/api/routes/	Get all travel routes
POST	/api/bookings/	Create a booking
GET	/api/bookings/{id}/	Get booking details

🚀 Deployment
Deploy on Render or Heroku

Uses gunicorn for production server

Environment variables are configured in the cloud platform

👨‍💻 Author
K Yashwant Kumar
2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the project root:

ini
Copy
Edit
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url
5️⃣ Run Migrations
bash
Copy
Edit
python manage.py migrate
6️⃣ Start the Development Server
bash
Copy
Edit
python manage.py runserver
🌐 API Endpoints
Method	Endpoint	Description
GET	/api/routes/	Get all travel routes
POST	/api/bookings/	Create a booking
GET	/api/bookings/{id}/	Get booking details

🚀 Deployment
Deploy on Render or Heroku

Uses gunicorn for production server

Environment variables are configured in the cloud platform

2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the project root:

ini
Copy
Edit
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url
5️⃣ Run Migrations
bash
Copy
Edit
python manage.py migrate
6️⃣ Start the Development Server
bash
Copy
Edit
python manage.py runserver
🌐 API Endpoints
Method	Endpoint	Description
GET	/api/routes/	Get all travel routes
POST	/api/bookings/	Create a booking
GET	/api/bookings/{id}/	Get booking details

🚀 Deployment
Deploy on Render or Heroku

Uses gunicorn for production server

Environment variables are configured in the cloud platform

👨‍💻 Author
K Yashwant Kumar
