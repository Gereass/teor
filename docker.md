### Docker: Основные команды [(на базу)](база.md)

Docker — это платформа для разработки, доставки и запуска приложений в изолированных контейнерах

#### 1. Управление контейнерами
- docker ps - показать запущенные контейнеры.
- docker ps -a - показать все контейнеры (включая остановленные).
- docker run <image> - запустить новый контейнер из образа.
- docker start <container> - запустить остановленный контейнер.
- docker stop <container> - остановить работающий контейнер.
- docker rm <container> - удалить контейнер.
- docker exec -it <container> <command> - выполнить команду внутри контейнера.
- docker logs <container> - показать логи контейнера.

#### 2. Управление образами
- docker images - показать список локальных образов.
- docker pull <image> - скачать образ из Docker Hub.
- docker build -t <name>:<tag> . - создать образ из Dockerfile.
- docker rmi <image> - удалить локальный образ.

#### 3. Сеть и тома
- docker network ls - показать список сетей.
- docker network create <network> - создать новую сеть.
- docker volume ls - показать список томов.
- docker volume create <volume> - создать новый том.
- docker run -v ~<host-path>:<container-path>~ - примонтировать директорию хоста в контейнер.

#### 4. Прочие команды
- docker inspect <container/image> - показать детальную информацию о контейнере или образе.
- docker stats - показать использование ресурсов контейнерами.
- docker system prune - очистить неиспользуемые образы, контейнеры, сети и тома.

---

### Docker Compose: Основные команды

#### 1. Запуск и управление сервисами
- docker-compose up - запустить все сервисы, описанные в docker-compose.yml.
- docker-compose up -d - запустить сервисы в фоновом режиме.
- docker-compose down - остановить и удалить контейнеры, сети и тома.
- docker-compose ps - показать состояние контейнеров для сервисов.

#### 2. Логи и выполнение команд
- docker-compose logs - показать логи всех сервисов.
- docker-compose logs <service> - показать логи конкретного сервиса.
- docker-compose exec <service> <command> - выполнить команду внутри контейнера сервиса.

#### 3. Пересборка и масштабирование
- docker-compose build - пересобрать образы для сервисов.
- docker-compose up --build - пересобрать и запустить сервисы.
- docker-compose scale <service>=<count> - масштабировать количество контейнеров для сервиса.

---

### Пример docker-compose.yml

version: '3.8'
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - app-network

  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - ENV_VAR=value
    depends_on:
      - db
    networks:
      - app-network

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - app-network

volumes:
  db-data:

networks:
  app-network:

---

### Полезные советы

1. Dockerfile:
   - FROM: базовый образ.
   - RUN: выполнить команду при сборке.
   - CMD: команда по умолчанию при запуске контейнера.
   - COPY: скопировать файлы в образ.
   - EXPOSE: указать порт для приложения.

2. Переменные окружения:
   - Используйте .env файл для хранения переменных:
     environment:
       - VAR_NAME=${VAR_VALUE}

3. Мониторинг:
   - Используйте docker stats для мониторинга ресурсов.
   - Интегрируйте Prometheus и Grafana для продвинутого мониторинга.

4. Очистка:
   - docker system prune -a - очистить все неиспользуемые ресурсы.
   - docker volume prune - очистить неиспользуемые тома.

5. Логирование:
   - Настройте драйверы логирования (json-file, syslog, fluentd) в docker-compose.yml.