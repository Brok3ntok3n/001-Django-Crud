# Catalógo de Productos

CRUD de productos hecho en Django (plantillas, Django Forms y ORM)

## Requisitos

- Python 3.10+

## Puesta en marcha
```bash
python -m venv venv
source venv/bin/activate        #Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rutas principales
- `/productos/`: listado
- `/productos/nuevo/`: alta
- `/admin/`: panel de administración