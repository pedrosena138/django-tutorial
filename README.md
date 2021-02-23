# First Django App (Work in Progress)

> Simple poll vote web page

## Requisites

1. [Python](https://www.python.org/) >= 3.x installed

## Initialization Step-by-Step

1. Clone the repository
2. Open your command prompt in the repository directory
3. Use the command:`python -m venv myvenv` to create your venv
4. Activate your venv:
   - Windows: `.\myvenv\Scripts\Activate.ps1`
   - Linux: `source myvenv/bin/activate`
5. Inside your venv install django, use the command: `pip install django`
   - Optional: Update pip using `pip install --upgrade pip`
6. Change to djangoApp directory: `cd djangoApp`
7. To apply the models use the command: `py manage.py makemigrations`
8. Then to sincronyze with the database use: `py manage.py migrate`
9. Now just start the server using: `py manage.py runserver`

## Documentation

- [PEP 405 -- Python Virtual Environments](https://www.python.org/dev/peps/pep-0405/)
- [Django Intro](https://docs.djangoproject.com/en/3.1/intro/)

---
