# [PYDEV](https://pydev.duckdns.org/)

PYDEV — это образовательная платформа, разработанная для обеспечения доступа к качественным 
и актуальным материалам по программированию и веб-разработке.
На платформе представлены руководства и учебные материалы по самым востребованным технологиям 
и инструментам, таким как Python, Docker, SQL, Git, HTML, CSS и JavaScript.

## Технологии

### Бекенд:
- Django
- PostgreSQL
- Nginx + Gunicorn
- Django REST Framework
- django-allauth (для аутентификации пользователей через внешние сервисы)

### Фронтенд:
- HTML, CSS (Bootstrap 5)
- JS

### Контейнеризация и управление:
- Docker
- Docker Compose

## Доступ

Проект доступен на [https://pydev.duckdns.org/](https://pydev.duckdns.org/)

## Как развернуть проект на сервере

1. Клонируйте репозиторий:

    ```shell
    git clone git@github.com:PchelaR/Pydev.git
    ```

2. Установите соединение с сервером:

    ```shell
    ssh username@server_address
    ```

3. Обновите индекс пакетов APT:

    ```shell
    sudo apt update
    ```

4. Отредактируйте файл `nginx/default.conf`:

    - В строках `server_name` укажите IP виртуальной машины (сервера).
    - Убедитесь, что у вас имеются SSL сертификаты.
    - В строках `ssl_certificate` и `ssl_certificate_key` укажите пути к вашим SSL сертификатам.

5. Проверьте наличие SSL сертификатов:

    Проверьте директорию, где хранятся сертификаты:

    ```shell
    ls /path/to/your/ssl/certificates/
    ```

6. Отредактируйте файл `settings.py`:

    Замените `yourdomain.com` на ваш домен:

    ```python
    ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

    CSRF_TRUSTED_ORIGINS = [
        'https://yourdomain.com',
        'https://yourdomain.com',
    ]
    ```

7. В директории `pydev_project` создайте файл `.env` и заполните его по аналогии:

    ```plaintext
    SECRET_KEY=secret_key

    DB_NAME=db_name
    DB_USER=db_user
    DB_PASSWORD=db_password
    DB_HOST=localhost
    DB_PORT=5432
    
    CLIENT_ID_GOOGLE=client_id_google
    SECRET_GOOGLE=secret_google
    
    CLIENT_ID_GITHUB=client_id_github
    SECRET_GITHUB=secret_github
    ```

8. Примените миграции:

    ```shell
    python3 manage.py makemigrations
    ```

    ```shell
    python3 manage.py migrate
    ```

9. Соберите и запустите проект с помощью Docker Compose:

    ```shell
    sudo docker-compose up -d --build
    ```

## Завершение

Проверьте, что все службы работают корректно и проверьте доступность вашего сайта по указанному URL.
