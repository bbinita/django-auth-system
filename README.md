# Django User Authentication System

A complete user authentication system built with Django, featuring user registration, login, logout functionality, and automated welcome emails. Designed with custom CSS for a clean, modern, and responsive user interface.

##  Features

-  **User Registration** - Sign up with username, email, and password
-  **User Login** - Secure authentication system
-  **User Logout** - Safe session termination
-  **Email Notifications** - Automated welcome emails upon registration
-  **Custom CSS Design** - Modern, responsive UI without Bootstrap
-  **Form Validation** - Real-time error handling and user feedback
-  **CSRF Protection** - Secure forms with Django CSRF tokens
-  **Mobile Responsive** - Works seamlessly on all devices

##  Tech Stack

- **Backend:** Django 4.x / Python 3.x
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (default, can be changed)
- **Email:** SMTP (Gmail)

##  Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/bbinita/django-auth-system.git
cd django-auth-system
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Configure Email Settings

#### Generate Gmail App Password

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Go to [App Passwords](https://myaccount.google.com/apppasswords)
4. Select **Mail** and your device
5. Click **Generate** and copy the 16-character password

#### Update `settings.py`

Add these settings to your `settings.py`:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-char-app-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`



##  Usage

### Register a New User

1. Navigate to `/register/`
2. Fill in username, email, and password
3. Submit the form
4. Check email for welcome message
5. Redirect to login page

### Login

1. Navigate to `/login/`
2. Enter username and password
3. Click "Login"
4. Redirect to homepage with welcome message

### Logout

1. Click "Logout" button in navbar
2. Confirm logout
3. Session terminated
4. Redirect to logout confirmation page

### Test Email Functionality

Visit `/test-email/` to send a test email and verify configuration



##  Security Features

-  Password hashing with Django's built-in system
-  CSRF protection on all forms
-  POST-only logout to prevent CSRF attacks
-  Secure session management
-  SQL injection protection via Django ORM
-  XSS protection with template escaping

##  Acknowledgments

- Django Documentation
- Django Community
- Font Awesome for icons

