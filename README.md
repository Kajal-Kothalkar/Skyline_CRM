# Skyline CRM

Skyline CRM is a lightweight Django-based customer relationship management system for tracking customer details, sales pipeline status, and interaction history.

## Features

- Dashboard with pipeline breakdown and recent activity
- Customer list, detail views, and editable records
- Interaction logging tied to each customer
- Admin interface for deeper management

## Getting Started

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Create an admin user (optional)

```bash
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

## Project Structure

- `skyline_crm/` - Project settings and URL configuration
- `crm/` - CRM app with models, views, templates, and admin
- `templates/` - Optional project-level templates (unused for now)

## Notes

- Default database is SQLite at `db.sqlite3`.
- Update `SECRET_KEY` and `DEBUG` before deploying to production.
