1. What base to use - PostgreSQL is nice-to-have. You have free choice! You can use SQLite.
2. Uploading an archive many times? Yes!
3. `pip freeze > requirements.txt` - to create a requirements.txt with your dependencies!
4. Do not include .idea or .vscode or __MACOSX__ folders in the zip. There is 10MB limit

https://www.guru99.com/download-install-postgresql.html


Table - citizen
    id - unique, autoincrement
    name
    city_id


Table cities
    id
    name
    country


base.html
    - defines blocks (placeholders, children must implement them)




base.html
{% load static %}
    {% block content %}
        Default value
    {%endblock}

    {% block additional_content %}



{% extends 'web/base.html' %}


    {% block content %}
        Children cool content!
    {%endblock}


    {% block css_files %}

    {%endblock}
















