# Список вопросов и ответов для собеседования на позицию Python-разработчик (Junior) [(на базу)](база.md)

### 1. Основы **Python**

#### Q1: Что такое **Python**?
**Python** — это высокоуровневый язык программирования общего назначения. Он известен своей простотой, читаемостью кода и универсальностью. **Python** используется для разработки веб-приложений, анализа данных, машинного обучения, автоматизации и многого другого.

#### Q2: Какие типы данных существуют в **Python**?
Основные типы данных:
- Числовые: `int`, `float`, `complex`.
- Строки: `str`.
- Последовательности: `list`, `tuple`, `range`.
- Множества: `set`, `frozenset`.
- Словари: `dict`.
- Логические значения: `bool` (*True*, *False*).
- NoneType: `None`.

#### Q3: Что такое **PEP 8**?
`PEP 8` (*Python Enhancement Proposal 8*) — это руководство по написанию читаемого и согласованного кода на **Python**. Оно включает рекомендации по форматированию кода, например:
- Использование 4 пробелов для отступов.
- Максимальная длина строки — 79 символов.
- Именование переменных в стиле *snake_case*.

#### Q4: Что такое `list comprehension` (тернарники)?
**List comprehension** — это компактный способ создания списков. Пример:
`squares = [x**2 for x in range(10)]`

#### Q5: Разница между `==` и `is`?
- `==` проверяет равенство значений.
- `is` проверяет, что два объекта ссылаются на один и тот же объект в памяти.

Пример:
```Python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True (значения равны)
print(a is c)  # False (разные объекты в памяти)
print(a is b)  # True (один и тот же объект)
```

### 2. Объектно-ориентированное программирование (ООП)
#### Q6: Что такое ООП?
ООП (объектно-ориентированное программирование) — это парадигма программирования, основанная на использовании объектов. Объекты объединяют данные (атрибуты) и поведение (методы).

#### Q7: Назовите основные принципы ООП.
1. *Инкапсуляция*: Сокрытие внутренней реализации объекта.
2. *Наследование*: Возможность создания новых классов на основе существующих.
3. *Полиморфизм*: Возможность использования одного интерфейса для разных типов данных.
4. *Абстракция*: Выделение ключевых характеристик объекта, игнорируя детали.

#### Q8: Что такое декораторы в Python?
Декораторы — это функции, которые позволяют модифицировать поведение других функций или методов без изменения их кода. Пример:
```Python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### 3. Базы данных

#### Q9: Что такое **SQL**?
**SQL (Structured Query Language)** — это язык запросов для работы с реляционными базами данных. Он используется для создания, обновления, удаления и выборки данных.

#### Q10: Разница между `JOIN` и `INNER JOIN`?
- *JOIN* по умолчанию означает *INNER JOIN*.
- *INNER JOIN* возвращает только те строки, где есть совпадения в обеих таблицах.

Пример:
```SQL
SELECT users.name, orders.order_id
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

#### Q11: Что такое **ORM**?
*ORM (Object-Relational Mapping)* — это технология, которая позволяет работать с базой данных как с объектами в коде. Например, *SQLAlchemy* — популярный *ORM* для *Python*.

### 4. Веб-разработка

#### Q12: Что такое *REST API*?
*REST (Representational State Transfer)* — это архитектурный стиль для создания веб-сервисов. *REST API* использует **HTTP-методы (GET, POST, PUT, DELETE)** для взаимодействия с сервером.

#### Q13: Как работает *HTTP*?
*HTTP (HyperText Transfer Protocol)* — это протокол для передачи данных между клиентом и сервером. Он работает по принципу "запрос-ответ":
- Клиент отправляет запрос (например, *GET* или *POST*).
- Сервер возвращает ответ (например, *HTML*-страницу или *JSON*).

#### Q14: Что такое *FastAPI*?
**FastAPI** — это современный фреймворк для создания *REST API* на Python. Он отличается высокой производительностью, поддержкой асинхронности и автоматической генерацией документации (Swagger).

### 5. Общие вопросы

#### Q15: Что такое **Git**?
*Git* — это система контроля версий, которая позволяет отслеживать изменения в коде, работать с ветками и сотрудничать с другими разработчиками.

#### Q16: Какие команды **Git** вы знаете?
Основные команды:
- `git init`: Инициализация нового репозитория.
- `git add`: Добавление файлов в индекс.
- `git commit`: Фиксация изменений.
- `git push`: Отправка изменений на удаленный репозиторий.
- `git pull`: Получение изменений с удаленного репозитория.

#### Q17: Что такое **Docker**?
*Docker* — это платформа для создания, доставки и запуска приложений в изолированных контейнерах. Контейнеры содержат все необходимое для работы приложения (код, библиотеки, зависимости).

#### Q18: Какие ошибки вы можете встретить при работе с *Python*?
Примеры ошибок:
- **SyntaxError**: Ошибка синтаксиса.
- **TypeError**: Операция применена к объекту несоответствующего типа.
- **KeyError**: Попытка доступа к несуществующему ключу в словаре.
- **IndexError**: Попытка доступа к несуществующему индексу в списке.

#### Q19: Как вы решаете задачи на собеседовании?
1. Читаю условие внимательно.
2. Задаю уточняющие вопросы.
3. Разрабатываю план решения.
4. Пишу код, начиная с простого варианта.
5. Тестирую решение на различных входных данных.

#### Q20: Какие проекты вы создавали на Python?
Пример ответа:
"Я создал веб-приложение на FastAPI для управления задачами. Приложение позволяет пользователям добавлять, редактировать и удалять задачи. Я использовал SQLite для хранения данных и Docker для развертывания."

#### [Некст левл плей](mid.md)