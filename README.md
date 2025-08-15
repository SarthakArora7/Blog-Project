# 📝 Full-Stack Blog Application

A **full-stack web blog application** built with:

- **Frontend:** React.js
- **Backend:** Django & Django REST Framework (DRF)
- **Database:** SQLite (Development)
- **API Communication:** REST API

---

## 📌 Features
- User authentication (register, login, logout)
- Create, read, update, and delete blog posts
- Rich text editor for blog content
- Responsive UI (mobile & desktop)
- API endpoints secured with token authentication

---

## 📂 Project Structure

my-blog/</br>
│</br>
├── backend/ # Django + DRF backend</br>
│ ├── manage.py</br>
│ ├── requirements.txt</br>
│ └── ...</br>
│</br>
├── frontend/ # React.js frontend</br>
│ ├── package.json</br>
│ ├── src/</br>
│ └── ...</br>
│</br>
├── .gitignore</br>
└── README.md</br>


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2️⃣ Backend Setup(Django + DRF)
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start backend server
python manage.py runserver
```
Backend runs on http://127.0.0.1:8000/ by default.

### 3️⃣ Frontend Setup(React)
```bash
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start
```
Frontend runs on http://localhost:3000/ by default.
