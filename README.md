# Nutri Connect 🍎

Welcome to **Nutri Connect** — a Django web app for exploring nutritious foods, searching food information, and chatting with an AI-powered nutrition assistant.

---

## 🚀 Features

- **User Registration & Login**
- **Searchable Food Gallery** (with images & nutrition details)
- **Admin Food Management**
- **AI Nutrition Chatbot** (OpenAI/Llama)
- **Responsive UI** (Bootstrap & Tailwind CSS)
- **Secure Authentication & CSRF Protection**

---

## ⚙️ Quickstart

1. **Clone the repo**
   ```sh
   git clone <repo-url>
   cd myproject
   ```
2. **Set up the virtual environment**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Mac/Linux
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up the database migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
5. Create a superuser
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

---

## 🔧 Configuration

Set up your environment variables in a `.env` file:

```env
SECRET_KEY="your-django-secret-key"
DEBUG=True
DEEPINFRA_API_KEY="your-deepinfrs-api-key"
DEEPINFRA_API_TOKEN="your-deepinfra-token"
DEEPINFRA_LANG_MODEL="your-llama-model"
PORT=8000
```
