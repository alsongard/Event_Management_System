# PROJECT OVERVIEW
This is an event management web application build with django templates for the frontend and django restframework specifically for admin and booking functionality. The web application enables user to create, login and register for an event

## OverView
This web application was an insight to the django rest framework for the backend.


## FEATURES
- **Backend**: RESTful APIs with Django REST Framework
- **Admin**: Custom admin interface for data management
- **Authentication**: [JWT/Session/Token-based]: Not yet implementted
- **Database**: Django rest-framework
- **API Documentation**: Auto-generated: Not yet implemented


## INSTALLATION

### Prerequisites
- Python 3.8+
- [Database] installed
- pip



### clone the repository
```bash
git clone "https://github.com/alsongard/Event_Management_System.git
```

### Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac

```pws
venv\Scripts\activate  # Windows
```
### Install dependencies
pip install -r requirements.txt

### Environment setup
cp .env.example .env
###  Edit .env with your settings

### Database setup
python manage.py migrate

## Create superuser
python manage.py createsuperuser

## Run development server
python manage.py runserver



# PROJECT STRUCTURE
```
event_system/
├── backend_api/
│   ├── init
│   ├── asgi
│   ├── settings
│   └── urls
│   └── wsgi
├── bookEvent/
|    └── migrations/
|    └── templates/
|    └── init
|    └── admin
|    └── models
|    └── apps
|    └── serializers
|    └── test
|    └── views
├── event_app/
|    └── migrations/
|    └── models/
|    └── apps
|    └── serializers
|    └── test
|    └── views
├── templates/
|   └── registration
|   └── base.html
|── userapp/
├── requirements.txt
└── manage.py
```
