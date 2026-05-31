# Tour UZ - Tour & Excursion Management Platform for Uzbekistan

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.x-green.svg)](https://www.djangoproject.com/)

**Tour UZ** is a Django-based web application for organizing and managing tours and excursions across Uzbekistan. The platform provides user management, an excursion catalog, booking functionality, and order processing.

## 🚀 Key Features

- **User Management** (`accounts`, `users`) — registration, authentication, user profiles
- **Excursion Catalog** (`excursions`) — add, edit, browse tours and excursions
- **Order Processing** (`orders`) — booking system, order status tracking, excursion integration
- **Responsive Frontend** — Django templates (`templates`), static files, and media uploads

## 🛠 Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript (likely Bootstrap)
- **Database:** (configurable — SQLite for development, PostgreSQL for production)
- **Environment:** venv, PowerShell/Batch scripts for automation

## 📁 Project Structure (Core Modules)
tour_uz/
├── accounts/ # Account management (login, registration)
├── excursions/ # Excursion models, views, and business logic
├── orders/ # Orders and booking management
├── users/ # User profiles and extended user models
├── templates/ # HTML templates
├── static/ # CSS, JavaScript, images
├── media/ # User-uploaded files (e.g., excursion photos)
├── tour_uz/ # Django project settings and configuration
├── manage.py # Django management entry point
└── .gitattributes # Git configuration


## 🧪 Quick Start Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/unk-leksi/tour_uz.git
   cd tour_uz
2. **Create and activate a virtual environment:**

bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
3. **Install dependencies:**

bash
pip install -r requirements.txt
(If requirements.txt doesn't exist yet, generate it with pip freeze > requirements.txt)

4. **Apply database migrations:**

bash
python manage.py migrate
5. **Create a superuser (admin account):**

bash
python manage.py createsuperuser

6. **Run the development server:**

bash
python manage.py runserver
Open your browser and navigate to: http://127.0.0.1:8000

📌 Project Status
This project is in its early stages (Initial commit). Active development is ongoing.

🤝 Contributing
Contributions and pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📄 License
(Add a license if you haven't already — e.g., MIT, GPL, etc.)

📬 Contact
Author: @unk-leksi

text

### How to add this README:

1. Go to your repository page: `https://github.com/unk-leksi/tour_uz`
2. Click **Add file** → **Create new file**
3. Name the file `README.md`
4. Copy and paste the English version above into the editor
5. Scroll down, write a commit message (e.g., "Add English README.md"), and click **Commit new file**
