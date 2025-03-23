# 📝 Django Blog Website

This is a Django-powered blog website where users can register, log in, create posts, comment on others' posts, and customize their profile. The UI includes modals, icons, and responsive styling to enhance the user experience.

---

## 🚀 Getting Started

Follow the steps below to get the project running locally.

---

### ✅ Prerequisites

Make sure you have the following installed:

- **Python** 3.10 or higher
- **pip** (Python package manager)
- **Git** (optional, for cloning the repo)
- **virtualenv** or `venv` for managing your virtual environment

---

### 📦 Installation

#### 1. Clone the repository or download the ZIP

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

#### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Activate (Mac/Linux)
source venv/bin/activate
# Activate (Windows)
venv\Scripts\activate
```

---

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

#### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

#### 5. Create a superuser (admin account)

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username and password.

---

#### 6. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to use the site.

---

## 🛠 Features

- User Registration & Login
- Create, Edit, and Delete Posts
- Commenting on Posts
- User Profiles with Custom Bio and Profile Picture
- Responsive UI with Bootstrap
- Modal Forms for Creating & Editing Posts

---

## 📂 Project Structure

```
blog_website/
├── blog/                   # App for blog logic
│   ├── templates/blog/     # HTML templates
│   ├── static/blog/        # Static files (CSS, images)
│   └── models.py           # Database models
├── blog_website/           # Project config
├── media/                  # Uploaded profile pictures
├── db.sqlite3              # SQLite database
├── requirements.txt        # Python dependencies
└── manage.py               # Django utility
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📃 License

[MIT License](LICENSE)

---

Happy coding! ✨
