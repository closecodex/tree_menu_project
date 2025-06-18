# Django Tree Menu

Приложение Django для отображения древовидного меню с гибкой настройкой через админку и кастомный template tag.

## 📌 Возможности

- Хранение структуры меню в базе данных
- Поддержка нескольких меню по имени (`{% draw_menu 'main_menu' %}`)
- Автоматическое определение активного пункта меню по URL
- Развёрнуто всё над активным пунктом и первый уровень под ним
- Поддержка вложенности любой глубины
- Переход по URL (как по обычным путям, так и по именованным URL Django)
- Всего 1 SQL-запрос на отрисовку меню
- Редактирование в стандартной админке Django

## 🚀 Инструкция по развертыванию

1. **Клонирование проекта**

```bash
git clone https://github.com/closecodex/tree_menu_project.git
cd tree_menu_project
```

2. **Создание виртуального окружения**
```bash
python -m venv venv
```

3. **Активация окружения**
- Windows:
```bash
venv\Scripts\activate
```

- macOS / Linux:
```bash
source venv/bin/activate
```

4. **Установка зависимостей**

```bash
pip install -r requirements.txt
```

5. **Применение миграций**

```bash
python manage.py migrate
```

6. **Создание суперпользователя**

```bash
python manage.py createsuperuser
```

7. **Запуск сервера**

```bash
python manage.py runserver
```

## Откройте сайт: http://127.0.0.1:8000

## 🛠 Использование

- Перейдите в админку: http://127.0.0.1:8000/admin/
- Создайте объект Menu (например, main_menu)
- Добавьте пункты меню (MenuItem), указывая вложенность через поле parent.
- В шаблоне подключите тег и отобразите меню:
  
```django
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```
