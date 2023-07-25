# Django MySQL full auth, with JWT

This is a full template of Django, working with **MySQL**, and a full functional authentication.

**IMPORTANT!!**
All the lines in comment in `models.py`, `serializer.py`, and `views.py` stand as an example of how to make your own model, its serializer, and its entry points.

## Instructions:

1. Set up a virtual env:

    ```python
    python -m venv env
    ```

2. Install the required requirements from `requirements.txt`:

    ```python
    pip install -r requirements.txt
    ```

3. Make migrations:

    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Make a superuser:

    ```python
    python manage.py createsuperuser
    ```

5. Run the server:

    ```python
    python manage.py runserver
    ```

