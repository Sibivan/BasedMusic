# 🎵 BasedMusic

**BasedMusic** — учебное веб-приложение на Django для ведения каталога музыкальных инструментов.

Проект был разработан в рамках студенческой работы и представляет собой небольшое CRUD-приложение с хранением данных в базе, загрузкой изображений, редактированием и удалением записей, автоматическим тестированием через GitHub Actions.

> 🇷🇺 **Русская версия** — основная.
> 🇬🇧 **English version** — ниже.

---

## 🇷🇺 Русская версия

### 📌 О проекте

BasedMusic — веб-приложение для учёта музыкальных инструментов.

Приложение позволяет добавлять инструменты в каталог, указывать их производителя и наличие на базе, загружать фотографии, а также отмечать дополнительные предметы, входящие в комплект.

Проект создавался как учебный для практического знакомства с **Python, Django, ORM, HTML/CSS, работой с базой данных, загрузкой файлов, тестированием и CI**.

### ✨ Возможности

* Добавление музыкального инструмента в каталог
* Выбор типа инструмента:

  * акустическая гитара
  * бас-гитара
  * электрогитара
* Указание производителя
* Загрузка фотографии инструмента
* Указание наличия инструмента на базе
* Указание комплектации:

  * дополнительные струны
  * медиатор
  * каподастр
* Просмотр каталога инструментов
* Редактирование существующих записей
* Удаление записей с подтверждением
* Хранение данных в SQLite
* Автоматический запуск тестов через GitHub Actions

### 🛠️ Технологии

| Технология          | Назначение                        |
| ------------------- | --------------------------------- |
| **Python**          | основной язык разработки          |
| **Django**          | backend и web framework           |
| **Django ORM**      | работа с базой данных             |
| **SQLite**          | база данных                       |
| **HTML / CSS**      | интерфейс                         |
| **Bootstrap 4**     | базовая стилизация интерфейса     |
| **Pillow**          | обработка загружаемых изображений |
| **Django TestCase** | автоматизированное тестирование   |
| **GitHub Actions**  | CI pipeline                       |

### 🏗️ Структура проекта

```text
BasedMusic/
├── basedapp/
│   ├── migrations/
│   ├── static/
│   │   └── basedapp/
│   │       └── css/
│   ├── templates/
│   │   └── basedapp/
│   │       ├── database.html
│   │       ├── delete.html
│   │       ├── index.html
│   │       └── update.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── basedmusic/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
│   └── images/
│
├── .github/
│   └── workflows/
│       └── django-ci.yml
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

### 🗄️ Модель данных

Основная сущность приложения — `Instrument`.

Для каждого инструмента хранятся:

* тип инструмента;
* производитель;
* изображение;
* наличие на базе;
* наличие дополнительных струн;
* наличие медиатора;
* наличие каподастра.

Модель реализована с использованием **Django ORM**.

### 🔄 CRUD

Приложение реализует основные CRUD-операции:

```text
Create → добавление инструмента
Read   → просмотр каталога
Update → редактирование инструмента
Delete → удаление инструмента
```

Для редактирования и удаления используются **Django Class-Based Views**, а добавление и отображение каталога реализованы через обычные Django views.

### 🖼️ Загрузка изображений

Для каждого инструмента можно загрузить изображение.

Файлы хранятся через Django `ImageField` в директории:

```text
media/images/
```

Для работы с изображениями используется **Pillow**.

### 🧪 Тестирование

В проекте присутствуют автоматизированные тесты на основе Django `TestCase`.

Проверяются, в частности:

* доступность главной страницы;
* доступность страницы каталога;
* добавление нового инструмента через POST-запрос;
* корректное сохранение данных в базе;
* обработка загружаемого изображения;
* redirect после добавления;
* удаление инструмента;
* уменьшение количества записей после удаления.

Запуск тестов:

```bash
python manage.py test
```

### ⚙️ Continuous Integration

Для проекта настроен **GitHub Actions CI pipeline**.

При push в `main` и при создании Pull Request выполняются:

1. получение исходного кода;
2. установка Python;
3. установка зависимостей;
4. выполнение Django migrations;
5. запуск автоматизированных тестов.

Pipeline использует Windows runner.

Workflow находится в:

```text
.github/workflows/django-ci.yml
```

### 🚀 Запуск проекта

#### 1. Клонирование репозитория

```bash
git clone https://github.com/Sibivan/BasedMusic.git
cd BasedMusic
```

#### 2. Создание виртуального окружения

Linux / macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

#### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

#### 4. Применение миграций

```bash
python manage.py migrate
```

#### 5. Запуск development-сервера

```bash
python manage.py runserver
```

После этого приложение будет доступно по адресу:

```text
http://127.0.0.1:8000/
```

### 📚 Чему был посвящён проект

Проект создавался прежде всего как практическая работа с Django и позволил получить опыт в:

* разработке web-приложений на Python;
* проектировании моделей и работе с ORM;
* создании CRUD-функциональности;
* работе с Django Forms;
* обработке загружаемых файлов;
* создании HTML-шаблонов;
* тестировании Django-приложений;
* настройке CI через GitHub Actions.

### 📌 Статус

**Учебный / завершённый проект.**

Проект не предназначен для production-использования и сохранён как часть учебного и проектного опыта.

---

# 🇬🇧 English Version

## 📌 About

**BasedMusic** is an educational Django web application for managing a catalog of musical instruments.

The application allows users to add instruments to the catalog, specify their manufacturer and availability, upload images, manage included accessories, edit existing entries and remove them.

The project was developed as a student project to gain practical experience with **Python, Django, ORM, databases, HTML/CSS, file uploads, automated testing and CI**.

## ✨ Features

* Add musical instruments to the catalog
* Select instrument type:

  * acoustic guitar
  * bass guitar
  * electric guitar
* Specify the manufacturer
* Upload an instrument image
* Track instrument availability
* Track included accessories:

  * additional strings
  * guitar pick
  * capo
* Browse the instrument catalog
* Edit existing entries
* Delete entries with confirmation
* Store data in SQLite
* Run automated tests through GitHub Actions

## 🛠️ Tech Stack

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| **Python**          | Main programming language |
| **Django**          | Web framework and backend |
| **Django ORM**      | Database interaction      |
| **SQLite**          | Database                  |
| **HTML / CSS**      | User interface            |
| **Bootstrap 4**     | UI styling                |
| **Pillow**          | Image handling            |
| **Django TestCase** | Automated testing         |
| **GitHub Actions**  | Continuous Integration    |

## 🏗️ Architecture

The project follows the standard Django project/application structure.

The main application is located in `basedapp/` and contains:

* Django models;
* forms;
* views;
* URL routing;
* templates;
* static files;
* database migrations;
* automated tests.

The `Instrument` model represents the main entity in the application.

## 🗄️ Data Model

Each instrument contains:

* instrument type;
* manufacturer;
* cover image;
* availability status;
* additional strings availability;
* guitar pick availability;
* capo availability.

The model is implemented using the **Django ORM**.

## 🔄 CRUD Operations

The application provides the complete CRUD workflow:

```text
Create → Add an instrument
Read   → Browse the catalog
Update → Edit an instrument
Delete → Remove an instrument
```

Django Class-Based Views are used for update and delete operations, while the catalog and creation flow are implemented using Django function-based views.

## 🖼️ Image Uploads

Users can upload an image for each instrument.

Images are stored using Django's `ImageField` under:

```text
media/images/
```

Image processing is handled with **Pillow**.

## 🧪 Testing

The project contains automated tests based on Django's `TestCase`.

The tests cover:

* main page availability;
* catalog page availability;
* instrument creation through POST requests;
* database persistence;
* uploaded image handling;
* redirects after creation;
* instrument deletion;
* database state after deletion.

Run the test suite with:

```bash
python manage.py test
```

## ⚙️ Continuous Integration

The project includes a **GitHub Actions CI pipeline**.

For pushes to `main` and pull requests targeting `main`, the workflow:

1. checks out the repository;
2. sets up Python;
3. installs dependencies;
4. applies Django migrations;
5. runs the automated test suite.

The workflow uses a Windows runner.

Workflow:

```text
.github/workflows/django-ci.yml
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sibivan/BasedMusic.git
cd BasedMusic
```

### 2. Create a virtual environment

Linux / macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 📚 Learning Outcomes

The project provided practical experience with:

* Python web development;
* Django application structure;
* Django ORM and database models;
* CRUD operations;
* Django Forms;
* file and image uploads;
* HTML templates;
* automated testing;
* Continuous Integration with GitHub Actions.

## 📌 Project Status

**Educational / completed project.**

BasedMusic was created as a student project and is preserved as part of the author's early development experience. It is not intended to be a production-ready application.
