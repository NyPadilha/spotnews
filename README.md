============================= Readme.md =============================
# :construction: CSS not Finished :construction:

# ProjectName (Trybe Project)

The application stores news that can be categorized by a registered user.

🚵 Worked Skills:

- Write applications using Django and Django Rest Framework
- Develop an application that uses the Model-View-Template architecture
- Work with MYSQL database

<details>
    <summary><strong>Portuguese Description</strong></summary></br>

    A aplicação armazena notícias que podem ser categorizadas por um usuário cadastrado.

    🚵 Habilidades trabalhadas:

    - Escrever aplicações usando Django e Django Rest Framework
    - Desenvolver uma aplicação que usa a arquitetura Model-View-Template
    - Trabalhar com banco de dados MYSQL
</details>

<br>

<details>
    <summary><strong>How to run</strong></summary></br>

    1. Clone this repository with:

        - `git clone git@github.com:NyPadilha/spotnews.git`
        - `cd  spotnews`

    Using Venv:

        1. Create the Virtual Environment:

            - `python3 -m venv .venv && source .venv/bin/activate`

        2. Install the dependencies:

            - `python3 -m pip install -r dev-requirements.txt`

    Without Venv:

        1. Install dependencies with:

            - `python3 -m pip install -r dev-requirements.txt`

    Run MYSQL Database With Docker:
      
        - `docker build -t spotnews-db .`
        - `docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db`

    Migrations:

        - `python3 manage.py makemigrations`
        - `python3 manage.py migrate` 
        - `python3 manage.py runscript seeds`

    Run the server:
      
        - `python3 manage.py runserver`

    Test:

        `python3 -m pytest`
</details>

<br>

## What I Coded

- news/models.py
- news/templates/home.html
- news/templates/news_details.html
- news/templates/categories_form.html
- news/templates/news_form.html
- news/serializers.py
- news/views.py

## What Trybe Coded

- Basically everything else