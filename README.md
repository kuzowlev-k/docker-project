# Практика по docker

## Описание проекта
Веб-сервис на Python (Flask), отображающий текущее московское время. 
Работает в двух Docker-контейнерах:
- **time-app** - Python приложение с Flask
- **nginx-container** - Nginx как обратный прокси

## Структура проекта
```
.
├── app/
│   └── app.py          # Flask приложение
├── default.conf         # Конфигурация Nginx
└── Dockerfile          # Инструкция для сборки образа
```

## Запуск

### 1. Создание сети
```bash
docker network create custom-network
```

### 2. Сборка и запуск приложения
```bash
docker build -t time-app .
docker run -d --name time-app --network custom-network time-app
```

### 3. Запуск Nginx
```bash
docker run -d \
    --name nginx-container \
    --network custom-network \
    --link time-app:time-app \
    -p 38080:80 \
    -v $(pwd)/default.conf:/etc/nginx/conf.d/default.conf:ro \
    nginx:latest
```

### 4. Проверка
Открыть в браузере:
- `http://localhost:38080` - текущее московское время
- `http://localhost:38080/?bg=red` - красный фон
- `http://localhost:38080/?bg=blue` - синий фон

## Docker Hub
https://hub.docker.com/repositories/kskuzovlev

## 5. Как выглядит работающее приложение 

<img width="1802" height="1017" alt="image" src="https://github.com/user-attachments/assets/186505ef-d78e-44e7-adf2-f5caf0c05de0" />
