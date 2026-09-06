# SecureFleet - IoT Device Management API

A REST API built with Django and Django REST Framework for managing IoT devices. I built this project to get hands-on experience with backend authentication systems, permissions, and API design - the kind of stuff that's actually used in real IoT/device management systems.

## Screenshots

**Dashboard**
![Dashboard](screenshots/dashboard.png)

**Admin Panel**
![Admin Panel](screenshots/admin-panel.png)

**API Response**
![API Response](screenshots/api-response.png)

**Login Page**
![Login Page](screenshots/login.png)

## What it does

- Full CRUD for devices (add, view, edit, delete) - through a browser dashboard and a REST API
- Three ways to authenticate depending on who's accessing it:
  - Session auth for the dashboard (browser)
  - Token auth for API/script access
  - JWT (access + refresh tokens) - more modern approach
- Only staff accounts can log into the Django admin panel, regular users have their own login
- API rate limiting so nobody can spam the endpoints (5 requests/min per user)
- Tested everything with Postman, and also wrote a small Python script that logs in and hits the API like a real device would

## Tech used

Python, Django, Django REST Framework, SQLite, HTML/CSS/JS for the dashboard, SimpleJWT for JWT auth.

## Running it locally

```bash
git clone https://github.com/rohitydv26122002-tech/SecureFleet-Django-API.git
cd SecureFleet-Django-API

python -m venv .venv
.venv\Scripts\Activate.ps1

pip install django djangorestframework djangorestframework-simplejwt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then go to:
- `/api/dashboard/` - the dashboard
- `/admin/` - admin panel
- `/api/devices/` - the API itself

## Getting an auth token

```
POST /api/token/           -> normal token
POST /api/jwt/token/       -> JWT (access + refresh)
```

Then send it with your requests:
```
Authorization: Token <your_token>
```
or for JWT:
```
Authorization: Bearer <your_access_token>
```

## API endpoints

| Method | Endpoint | What it does |
|--------|----------|---------------|
| GET | /api/devices/ | list all devices |
| POST | /api/devices/ | add a new device |
| GET | /api/devices/{id}/ | get one device |
| PUT | /api/devices/{id}/ | update a device |
| DELETE | /api/devices/{id}/ | delete a device |
| POST | /api/token/ | get a token |
| POST | /api/jwt/token/ | get a JWT pair |
| POST | /api/jwt/refresh/ | refresh access token |

All of the above (except getting tokens) need auth.

## Why I built it this way

Most tutorial projects just do basic CRUD with one login system. I wanted to actually understand *why* you'd pick session auth vs token vs JWT, so I implemented all three for different use cases - dashboard vs API vs simulated device access. Same thing with throttling and admin permissions - trying to build something closer to how it'd actually work in production, not just a toy project.

---
Rohit Yadav - [LinkedIn](https://www.linkedin.com/in/rohit-yadav-23707639a) - [GitHub](https://github.com/rohitydv26122002-tech)