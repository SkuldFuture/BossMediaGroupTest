## Начало
```env
создайте `.env` файл в корне проекта и заполните его переменными окружения 
на примере существующего `.env.example`, кроме поля DATABASE_HOST
```

## Запуск
```bash
  docker compose up --build
```
Если ругается на то что не бек не может подключиться к бд, то запустите в корне проекта docker-compose down -v 

## Роут Админки
```bash
http://{backend_host}:{port}/admin/
Логин и пароль для входа задаются в .env файле
```

## Роут Сваггера
```bash
http://{backend_host}:{port}/admin/
```
